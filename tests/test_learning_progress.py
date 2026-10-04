"""Check portable progress through its public save/resume commands."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/paper-tutor/scripts/progress.py"


def record():
    return {
        "version": 1,
        "source": {"title": "Selected paper", "path": "paper.txt", "coverage": "Section 2 only"},
        "position": {"target": "What does the observation establish?", "location": "Section 2"},
        "explained": ["Observed association differs from a causal claim."],
        "understanding": [{"point": "Association versus causation", "status": "explained_unverified",
                           "answer": "I understand.", "reason": "No reasoning check supplied."}],
        "gaps": ["How the design supports a causal claim remains unverified."],
        "next_entry": "Return to the design and its inference limits.",
    }


class LearningProgressCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.draft = self.directory / "draft.json"
        self.output = self.directory / "progress.json"
        self.source = self.directory / "paper.txt"
        self.source.write_text("Section 2: The observation is an association.", encoding="utf-8")

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True, encoding="utf-8")

    def write_draft(self, data):
        self.draft.write_text(json.dumps(data), encoding="utf-8")

    def test_saved_record_reopens_with_source_and_preserves_unverified_gap(self):
        self.write_draft(record())
        saved = self.run_cli("save", self.draft, "--output", self.output)
        self.assertEqual(saved.returncode, 0, saved.stderr)
        self.assertEqual(json.loads(self.output.read_text(encoding="utf-8")), record())
        resumed = self.run_cli("resume", self.output)
        self.assertEqual(resumed.returncode, 0, resumed.stderr)
        bundle = json.loads(resumed.stdout)
        self.assertEqual(bundle["progress"]["understanding"][0]["status"], "explained_unverified")
        self.assertEqual(bundle["progress"]["gaps"], record()["gaps"])
        self.assertEqual(bundle["source_text"], "Section 2: The observation is an association.")

    def test_mastery_requires_specific_answer_evidence_and_preserves_existing_file_on_error(self):
        data = record()
        data["understanding"][0].update(status="mastered", answer="")
        self.write_draft(data)
        self.output.write_text("existing progress", encoding="utf-8")
        result = self.run_cli("save", self.draft, "--output", self.output)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("answer", result.stderr)
        self.assertEqual(self.output.read_text(encoding="utf-8"), "existing progress")

    def test_save_cannot_overwrite_paper_source_or_input_draft(self):
        self.write_draft(record())
        for destination in (self.source, self.draft):
            before = destination.read_text(encoding="utf-8")
            result = self.run_cli("save", self.draft, "--output", destination)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(destination.read_text(encoding="utf-8"), before)

    def test_resume_requests_readable_source_without_losing_progress(self):
        data = record()
        data["source"]["path"] = None
        self.write_draft(data)
        self.assertEqual(self.run_cli("save", self.draft, "--output", self.output).returncode, 0)
        result = self.run_cli("resume", self.output)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--source", result.stderr)
        self.assertEqual(result.stdout, "")
        before = self.output.read_text(encoding="utf-8")
        resumed = self.run_cli("resume", self.output, "--source", self.source)
        self.assertEqual(resumed.returncode, 0, resumed.stderr)
        self.assertEqual(self.output.read_text(encoding="utf-8"), before)
        self.assertEqual(json.loads(resumed.stdout)["progress"]["next_entry"], data["next_entry"])

    def test_resume_requires_actual_nonempty_source_not_the_progress_file(self):
        self.write_draft(record())
        self.assertEqual(self.run_cli("save", self.draft, "--output", self.output).returncode, 0)
        before = self.output.read_bytes()
        self.source.unlink()
        missing = self.run_cli("resume", self.output)
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("--source", missing.stderr)
        self.source.write_text("  \n", encoding="utf-8")
        empty = self.run_cli("resume", self.output)
        self.assertNotEqual(empty.returncode, 0)
        self.assertIn("empty", empty.stderr)
        same = self.run_cli("resume", self.output, "--source", self.output)
        self.assertNotEqual(same.returncode, 0)
        self.assertIn("not paper evidence", same.stderr)
        self.assertEqual(self.output.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
