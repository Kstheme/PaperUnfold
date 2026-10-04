"""Save a portable learning record or read it together with its readable source."""
import argparse
import json
from pathlib import Path
import sys


def read_record(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("version") != 1:
        raise ValueError("Expected a version 1 progress object.")
    def text(value, name, allow_empty=False):
        if not isinstance(value, str) or (not allow_empty and not value.strip()):
            raise ValueError(f"{name} must be {'a string' if allow_empty else 'a nonempty string'}.")

    for field, keys in (("source", ("title", "coverage")), ("position", ("target", "location"))):
        obj = data.get(field)
        if not isinstance(obj, dict):
            raise ValueError(f"{field} must be an object.")
        for key in keys:
            text(obj.get(key), f"{field}.{key}")
    source_path = data["source"].get("path")
    if source_path is not None:
        text(source_path, "source.path")
    for field in ("explained", "gaps", "understanding"):
        if not isinstance(data.get(field), list):
            raise ValueError(f"{field} must be a list.")
    for field in ("explained", "gaps"):
        for item in data[field]:
            text(item, field)
    for item in data["understanding"]:
        if not isinstance(item, dict):
            raise ValueError("Each understanding item must be an object.")
        text(item.get("point"), "understanding.point")
        if item.get("status") not in ("explained_unverified", "partial", "mastered"):
            raise ValueError("Unknown understanding.status.")
        text(item.get("answer"), "understanding.answer", item["status"] == "explained_unverified")
        text(item.get("reason"), "understanding.reason")
    text(data.get("next_entry"), "next_entry")
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    save = commands.add_parser("save", help="Save a draft record to the specified progress file.")
    save.add_argument("record", type=Path)
    save.add_argument("--output", type=Path, required=True)
    resume = commands.add_parser("resume", help="Read progress and its source; writes no files.")
    resume.add_argument("record", type=Path)
    resume.add_argument("--source", type=Path, help="Readable UTF-8 source supplied for this session.")
    args = parser.parse_args()
    try:
        data = read_record(args.record)
        if args.command == "save":
            protected = {args.record.resolve()}
            if data["source"].get("path"):
                protected.add((args.output.parent / data["source"]["path"]).resolve())
                protected.add((args.record.parent / data["source"]["path"]).resolve())
            if args.output.resolve() in protected:
                raise ValueError("Progress output must differ from the source and input draft.")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Saved progress: {args.output.resolve()}")
        else:
            source_path = data["source"].get("path")
            if args.source is None and source_path is None:
                raise ValueError("Readable paper source is missing; supply --source <source.txt>.")
            source = args.source or args.record.parent / source_path
            if source.resolve() == args.record.resolve():
                raise ValueError("Progress is not paper evidence; supply --source <source.txt>.")
            try:
                source_text = source.read_text(encoding="utf-8")
            except OSError as error:
                raise ValueError("Readable paper source is unavailable; supply --source <source.txt>.") from error
            if not source_text.strip():
                raise ValueError("Readable paper source is empty; supply --source <source.txt>.")
            print(json.dumps({"progress": data, "source_path": str(source.resolve()),
                              "source_text": source_text}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Progress error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
