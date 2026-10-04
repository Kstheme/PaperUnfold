"""Remote-input CLI acceptance tests over actual HTTP and saved material."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from test_pdf_input import synthetic_pdf

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/paper-guide/scripts/fetch_remote.py"


class RemoteInputCLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as temp:
            pdf = Path(temp) / "paper.pdf"
            synthetic_pdf(pdf, ["Synthetic online method.", "Synthetic online result may vary."])
            cls.pdf_bytes = pdf.read_bytes()
            synthetic_pdf(pdf, [""])
            cls.scanned_bytes = pdf.read_bytes()
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *_):
                pass

            def do_GET(self):
                if self.path == "/redirect":
                    self.send_response(302)
                    self.send_header("Location", "/article")
                    self.end_headers()
                    return
                pages = {"/article": b'<html><title>Synthetic research</title><nav>Site menu</nav><article><h1>Study</h1><h2>Methods</h2><p>We compared two synthetic groups.</p><h2>Results</h2><p>The result may depend on conditions.</p></article><script>invented()</script></html>',
                         "/landing": b'<html><meta name="citation_pdf_url" content="/paper.pdf"><article><h1>Abstract</h1><p>Abstract of a synthetic study.</p></article></html>',
                         "/metadata": b'<html><title>Metadata only</title><meta name="citation_pdf_url" content="/paper.pdf"></html>',
                         "/abstract": b'<html><title>Synthetic abstract only</title><meta name="citation_pdf_url" content="/blocked.pdf"><article><h1>Abstract</h1><p>Only a synthetic abstract is accessible.</p></article></html>',
                         "/title-only": b'<html><title>Unseen full paper title</title></html>',
                         "/bad-linked": b'<html><meta name="citation_pdf_url" content="/scan.pdf"><article><h1>Abstract</h1><p>Accessible abstract despite unreadable PDF.</p></article></html>',
                         "/scan.pdf": cls.scanned_bytes,
                         "/paper.pdf": cls.pdf_bytes}
                if self.path not in pages:
                    self.send_error(403, "Full text unavailable")
                    return
                self.send_response(200)
                self.send_header("Content-Type", "application/pdf" if self.path.endswith(".pdf") else "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(pages[self.path])
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def run_fetch(self, path):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        output = Path(temporary.name) / "material.json"
        result = subprocess.run([sys.executable, str(SCRIPT), self.base + path,
                                 "--output", str(output)], capture_output=True,
                                text=True, encoding="utf-8")
        self.assertTrue(output.exists(), result.stderr)
        return result, json.loads(output.read_text(encoding="utf-8")), output

    def test_redirect_reads_actual_web_body_with_resolved_provenance(self):
        result, material, _ = self.run_fetch("/redirect")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(material["provenance"]["resolved_url"], self.base + "/article")
        self.assertIn("We compared two synthetic groups.", material["source"]["text"])
        self.assertNotIn("Site menu", material["source"]["text"])
        self.assertNotIn("invented", material["source"]["text"])
        self.assertIn("Methods", material["source"]["text"])
        self.assertTrue(material["source"]["missing"])

    def test_landing_metadata_locates_but_only_pdf_supplies_body_and_pages(self):
        result, material, output = self.run_fetch("/landing")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Synthetic online method.", material["source"]["text"])
        self.assertNotIn("Abstract of", material["source"]["text"])
        self.assertEqual(material["readable_pages"], [1, 2])
        self.assertEqual(material["provenance"]["landing_url"], self.base + "/landing")
        self.assertEqual(material["provenance"]["resolved_url"], self.base + "/paper.pdf")
        self.assertTrue(Path(material["provenance"]["downloaded_pdf"]).exists())

    def test_title_metadata_is_only_locator_but_can_lead_to_readable_pdf(self):
        result, material, _ = self.run_fetch("/metadata")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Synthetic online method.", material["source"]["text"])
        self.assertEqual(material["provenance"]["resolved_url"], self.base + "/paper.pdf")

    def test_direct_online_pdf_keeps_actual_pages_and_local_inspection_copy(self):
        result, material, _ = self.run_fetch("/paper.pdf")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(material["status"], "readable")
        self.assertEqual(material["pages"][1]["pdf_page"], 2)
        self.assertIn("[PDF page 2 of 2]", material["source"]["text"])

    def test_abstract_survives_blocked_pdf_with_explicit_limited_coverage(self):
        result, material, _ = self.run_fetch("/abstract")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(material["status"], "partial")
        self.assertIn("Only a synthetic abstract", material["source"]["text"])
        self.assertEqual(material["provenance"]["pdf_attempts"][0]["status"], "unavailable")
        self.assertTrue(any("Linked PDF" in x for x in material["source"]["missing"]))
        self.assertNotIn("pages", material)

    def test_http_denial_is_actionable_failure_without_invented_body_or_guide(self):
        result, material, _ = self.run_fetch("/denied")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(material["status"], "unreadable")
        self.assertEqual(material["source"]["text"], "")
        self.assertIn("403", material["error"])
        self.assertIn("readable", material["error"])
        self.assertNotIn("sections", material)

    def test_title_is_not_read_body_when_no_readable_material_returned(self):
        result, material, _ = self.run_fetch("/title-only")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(material["source"]["text"], "")
        self.assertIn("metadata", material["error"])

    def test_unreadable_linked_pdf_retains_readable_landing_text_and_its_provenance(self):
        result, material, _ = self.run_fetch("/bad-linked")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(material["status"], "partial")
        self.assertIn("Accessible abstract despite", material["source"]["text"])
        self.assertEqual(material["provenance"]["resolved_url"], self.base + "/bad-linked")
        self.assertEqual(material["provenance"]["pdf_attempts"][0]["status"], "unreadable")
        self.assertIn("OCR", material["provenance"]["pdf_attempts"][0]["error"])


if __name__ == "__main__":
    unittest.main()
