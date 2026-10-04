"""Copy independent PaperUnfold skills from this checkout to an explicit skills directory."""
import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("paper-guide", "paper-tutor")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", required=True, type=Path, help="Skills parent, e.g. <project>/.agents/skills")
    parser.add_argument("--skill", action="append", choices=SKILLS, help="Install only this skill; repeat to select both")
    args = parser.parse_args()
    destination = args.dest.expanduser().resolve()
    selected = list(dict.fromkeys(args.skill or SKILLS))
    try:
        if not (ROOT / "LICENSE").is_file():
            raise ValueError("The checkout's project LICENSE is missing.")
        for name in SKILLS:
            source = (ROOT / "skills" / name).resolve()
            if destination == source or source in destination.parents:
                raise ValueError("Choose a destination outside the source skill packages.")
        for name in selected:
            target = destination / name
            if target.exists() or target.is_symlink():
                raise ValueError(f"{target} already exists. Choose an empty destination; installed skills are preserved.")
            if not (ROOT / "skills" / name / "SKILL.md").is_file():
                raise ValueError(f"Source package {name} is missing SKILL.md.")
        for name in selected:
            shutil.copytree(ROOT / "skills" / name, destination / name,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo"))
            shutil.copy2(ROOT / "LICENSE", destination / name / "LICENSE")
            print(f"Installed {name}: {destination / name / 'SKILL.md'}")
    except (OSError, ValueError) as error:
        print(f"Cannot install skills: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
