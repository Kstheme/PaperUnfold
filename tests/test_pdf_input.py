"""Public local-PDF CLI tests using tiny, explicitly synthetic PDF inputs."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from pypdf import PdfWriter
from pypdf.generic import DictionaryObject, NameObject, DecodedStreamObject

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/paper-guide/scripts/extract_pdf.py"


def synthetic_pdf(path, page_texts, encrypted=False):
    writer = PdfWriter()
    for text in page_texts:
        page = writer.add_blank_page(width=612, height=792)
        if text:
            font = DictionaryObject({NameObject("/Type"): NameObject("/Font"),
                                     NameObject("/Subtype"): NameObject("/Type1"),
                                     NameObject("/BaseFont"): NameObject("/Helvetica")})
            page[NameObject("/Resources")] = DictionaryObject({NameObject("/Font"):
                DictionaryObject({NameObject("/F1"): writer._add_object(font)})})
            content = DecodedStreamObject()
            content.set_data(f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET".encode("ascii"))
            page[NameObject("/Contents")] = writer._add_object(content)
    if encrypted:
        writer.encrypt("synthetic-test-password")
    with path.open("wb") as stream:
        writer.write(stream)


class LocalPDFCLI(unittest.TestCase):
    def run_extraction(self, pages=None, malformed=False, encrypted=False):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        directory = Path(temporary.name)
        pdf, output = directory / "synthetic.pdf", directory / "material.json"
        if malformed:
            pdf.write_bytes(b"This is not a PDF.")
        else:
            synthetic_pdf(pdf, pages or [], encrypted=encrypted)
        result = subprocess.run([sys.executable, str(SCRIPT), str(pdf), "--output", str(output)],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertTrue(output.exists(), result.stderr)
        return result, json.loads(output.read_text(encoding="utf-8"))

    def test_readable_text_keeps_actual_pdf_page_locations(self):
        result, material = self.run_extraction(["1 Introduction. Synthetic premise.",
                                                "2 Conclusion. Synthetic result may vary."])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(material["status"], "readable")
        self.assertEqual(material["page_count"], 2)
        self.assertEqual(material["readable_pages"], [1, 2])
        self.assertEqual(material["pages"][1]["pdf_page"], 2)
        self.assertIn("Synthetic result may vary.", material["source"]["text"])
        self.assertIn("[PDF page 2 of 2]", material["source"]["text"])
        self.assertIn("original", material["source"]["coverage"])
        self.assertTrue(material["source"]["missing"])

    def test_partial_input_reports_unreadable_page_without_invented_content(self):
        result, material = self.run_extraction(["Synthetic introduction only.", ""])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(material["status"], "partial")
        self.assertEqual(material["readable_pages"], [1])
        self.assertEqual(material["pages"][1]["status"], "no_text")
        self.assertEqual(material["pages"][1]["text"], "")
        self.assertTrue(any("2" in x and "OCR" in x for x in material["source"]["missing"]))

    def test_no_text_returns_actionable_failure_report_and_no_guide(self):
        result, material = self.run_extraction([""])
        self.assertEqual(result.returncode, 2)
        self.assertEqual(material["status"], "unreadable")
        self.assertEqual(material["source"]["text"], "")
        self.assertIn("OCR", result.stderr)
        self.assertNotIn("thread", material)
        self.assertNotIn("sections", material)

    def test_corrupt_pdf_reports_failure_without_traceback(self):
        result, material = self.run_extraction(malformed=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(material["status"], "unreadable")
        self.assertIn("open", material["error"])
        self.assertNotIn("Traceback", result.stderr)

    def test_encrypted_pdf_requires_unlocked_copy(self):
        result, material = self.run_extraction(["Synthetic protected text."], encrypted=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("unlocked", material["error"])
        self.assertEqual(material["source"]["text"], "")

    def test_input_output_collision_preserves_pdf(self):
        with tempfile.TemporaryDirectory() as temp:
            pdf = Path(temp) / "synthetic.pdf"
            synthetic_pdf(pdf, ["Synthetic text."])
            before = pdf.read_bytes()
            result = subprocess.run([sys.executable, str(SCRIPT), str(pdf), "--output", str(pdf)],
                                    capture_output=True, text=True, encoding="utf-8")
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(pdf.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
