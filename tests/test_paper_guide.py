"""Check the public renderer CLI and the saved reading artifact."""
import json
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/paper-guide/scripts/render_guide.py"


class Artifact(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.tags = set(), [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))


def guide():
    return {
        "title": "A selected passage", "language": "en",
        "source": {"name": "User-provided passage", "text": "The estimate may change if the sample is small.",
                   "coverage": "One pasted paragraph only.", "missing": ["Remaining paper unavailable."]},
        "evidence": [{"id": "e1", "location": "Pasted paragraph 1", "quote": "may change if the sample is small"}],
        "thread": [{"kind": "author", "text": "The estimate may change if the sample is small.", "evidence": ["e1"]}],
        "sections": [{"id": "argument", "title": "Argument", "role": "Describes a limitation.",
                      "points": [{"kind": "inference", "text": "This is a conditional claim.", "evidence": ["e1"]}]}],
        "terms": [{"original": "estimate", "name": "estimate", "essential": True,
                   "explanation": {"kind": "background", "text": "A quantity inferred from observations.", "evidence": []}}],
    }


class GuideCLI(unittest.TestCase):
    def render(self, data):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        directory = Path(temp.name)
        data_file, output = directory / "guide.json", directory / "guide.html"
        data_file.write_text(json.dumps(data), encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCRIPT), str(data_file), "--output", str(output)],
                                capture_output=True, text=True, encoding="utf-8")
        return result, output

    def test_saveable_guide_has_working_local_targets_and_native_controls(self):
        result, output = self.render(guide())
        self.assertEqual(result.returncode, 0, result.stderr)
        html = output.read_text(encoding="utf-8")
        artifact = Artifact()
        artifact.feed(html)
        self.assertTrue(artifact.links)
        for link in artifact.links:
            self.assertTrue(link.startswith("#"), link)
            self.assertIn(link[1:], artifact.ids)
        self.assertGreaterEqual(artifact.tags.count("details"), 2)
        self.assertEqual(artifact.tags.count("details"), artifact.tags.count("summary"))
        self.assertIn("One pasted paragraph only.", html)
        self.assertIn("Remaining paper unavailable.", html)
        self.assertIn("may change if the sample is small", html)
        self.assertNotIn('src="http', html)

    def test_source_markup_is_visible_text_and_language_is_preserved(self):
        data = guide()
        data["title"] = '<script>alert("x")</script>'
        data["language"] = "zh-CN"
        result, output = self.render(data)
        self.assertEqual(result.returncode, 0, result.stderr)
        html = output.read_text(encoding="utf-8")
        self.assertIn('lang="zh-CN"', html)
        self.assertIn("原文陈述", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertNotIn('<script>alert(', html)

    def test_untraceable_evidence_fails_without_creating_html(self):
        data = guide()
        data["evidence"][0]["quote"] = "invented paper result"
        result, output = self.render(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())
        self.assertIn("quote", result.stderr.lower())

    def test_author_claim_requires_a_real_evidence_reference(self):
        data = guide()
        data["thread"][0]["evidence"] = ["unknown"]
        result, output = self.render(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())
        self.assertIn("references", result.stderr.lower())

    def test_another_language_requires_localized_controls(self):
        data = guide()
        data["language"] = "fr"
        result, output = self.render(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())
        self.assertIn("labels", result.stderr)
        data["labels"] = {
            "coverage": "Périmètre", "missing": "Absent", "thread": "Fil de recherche",
            "contents": "Sommaire", "terms": "Termes", "evidence": "Extraits",
            "source": "Texte fourni", "role": "Rôle / interprétation",
            "essential": "Essentiel", "optional": "Facultatif", "author": "Auteur",
            "background": "Contexte", "inference": "Interprétation", "analogy": "Analogie",
        }
        result, output = self.render(data)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Périmètre", output.read_text(encoding="utf-8"))

    def test_empty_paper_text_cannot_generate_a_reading_claim(self):
        data = guide()
        data["source"]["text"] = " "
        result, output = self.render(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())
        self.assertIn("source.text", result.stderr)

    def test_math_guide_embeds_offline_renderer_but_keeps_source_verbatim(self):
        data = guide()
        data["sections"][0]["points"][0]["text"] = r'Inline \(d_k\). Display \[\frac{QK^T}{\sqrt{d_k}}\].'
        result, output = self.render(data)
        self.assertEqual(result.returncode, 0, result.stderr)
        content = output.read_text(encoding="utf-8")
        self.assertIn('renderMathInElement', content)
        self.assertIn('data:font/woff2;base64,', content)
        self.assertIn('class="math-content"', content)
        self.assertNotIn('<script src=', content)
        self.assertNotIn('url(fonts/', content)
        self.assertIn('<pre>' + data["source"]["text"] + '</pre>', content)

    def test_prose_only_guide_does_not_embed_math_assets(self):
        result, output = self.render(guide())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('renderMathInElement', output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
