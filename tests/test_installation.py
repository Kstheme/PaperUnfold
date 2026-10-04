"""Check installed skill packages through their public commands outside the checkout."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from test_paper_guide import guide

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / "scripts/install_skills.py"


class InstallationCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="paperunfold-install-")
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        self.destination = self.project / ".agents/skills"

    def command(self, *args):
        return subprocess.run([sys.executable, "-X", "utf8", *map(str, args)],
                              cwd=self.project, capture_output=True, text=True, encoding="utf-8")

    def test_independent_tutor_install_saves_and_resumes_without_repo_or_guide(self):
        result = self.command(INSTALL, "--dest", self.destination, "--skill", "paper-tutor")
        self.assertEqual(result.returncode, 0, result.stderr)
        tutor = self.destination / "paper-tutor"
        self.assertTrue((tutor / "SKILL.md").is_file())
        self.assertTrue((tutor / "LICENSE").is_file())
        self.assertFalse((self.destination / "paper-guide").exists())
        source = self.project / "paper.txt"
        source.write_text("The study measured an association, not an intervention.", encoding="utf-8")
        draft = self.project / "draft.json"
        draft.write_text(json.dumps({"version": 1,
            "source": {"title": "Supplied paper passage", "path": "paper.txt", "coverage": "One passage"},
            "position": {"target": "Association versus intervention", "location": "Supplied paragraph"},
            "explained": ["An association is not a causal effect"],
            "understanding": [{"point": "Causal interpretation", "status": "explained_unverified", "answer": "", "reason": "No answer yet"}],
            "gaps": ["Causal reasoning remains unchecked"], "next_entry": "Check the distinction"}), encoding="utf-8")
        progress = self.project / "progress.json"
        saved = self.command(tutor / "scripts/progress.py", "save", draft, "--output", progress)
        self.assertEqual(saved.returncode, 0, saved.stderr)
        resumed = self.command(tutor / "scripts/progress.py", "resume", progress)
        self.assertEqual(resumed.returncode, 0, resumed.stderr)
        bundle = json.loads(resumed.stdout)
        self.assertEqual(bundle["source_text"], source.read_text(encoding="utf-8"))
        self.assertEqual(bundle["progress"]["understanding"][0]["status"], "explained_unverified")

    def test_existing_skill_stops_before_installing_any_selected_package(self):
        existing = self.destination / "paper-tutor"
        existing.mkdir(parents=True)
        marker = existing / "my-customization.txt"
        marker.write_text("Keep my installed skill", encoding="utf-8")
        result = self.command(INSTALL, "--dest", self.destination)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(encoding="utf-8"), "Keep my installed skill")
        self.assertFalse((self.destination / "paper-guide").exists())

    def test_independent_guide_install_renders_math_with_its_own_offline_assets(self):
        result = self.command(INSTALL, "--dest", self.destination, "--skill", "paper-guide")
        self.assertEqual(result.returncode, 0, result.stderr)
        package = self.destination / "paper-guide"
        self.assertFalse((self.destination / "paper-tutor").exists())
        data = guide()
        data["sections"][0]["points"].append({"kind": "background", "text": r"Notation: \(x^2\).", "evidence": []})
        request = self.project / "guide.json"
        request.write_text(json.dumps(data), encoding="utf-8")
        output = self.project / "guide.html"
        rendered = self.command(package / "scripts/render_guide.py", request, "--output", output)
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        content = output.read_text(encoding="utf-8")
        self.assertIn("renderMathInElement", content)
        self.assertIn("data:font/woff2;base64,", content)
        self.assertNotIn("<script src=", content)
        self.assertTrue((package / "assets/katex/LICENSE").is_file())


if __name__ == "__main__":
    unittest.main()
