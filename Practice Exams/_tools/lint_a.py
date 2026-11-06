"""Lint short answers (Python only).

Official key formats: keys-交大.tsv has a 題目ID/答案/來源檔 header.
Uppercase (X) groups form a selection; 或 separates alternative selections;
均給分 follows the full option list. Grouped answers use Qn: selections.
Normalization ignores whitespace, trailing Markdown line-break backslashes,
and > 註： lines. Grouped newlines and semicolons are equivalent; selection
order, alternative order, question numbers, and all other text remain exact.

Usage: python3 lint_a.py [--all] [ID ...]
No IDs checks existing _a/*.md; --all also reports missing in-scope answers.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "_src"
ADIR = SRC / "_a"
QDIR = SRC / "_q"
KEYS = SRC / "_index" / "keys-交大.tsv"
MARKERS = {f"<!-- src: {source} -->": source for source in ("official", "drive", "devin")}
SELECTION = r"(?:\([A-Z]\))+"
CHOICE = rf"{SELECTION}(?:或{SELECTION})*(?:均給分)?"
GROUPED = rf"Q\d+:{CHOICE}(?:;Q\d+:{CHOICE})*"


def normalize(body):
    lines = []
    for line in body.splitlines():
        if line.lstrip().startswith("> 註："):
            continue
        line = re.sub(r"\s+", "", line).rstrip("\\")
        if line:
            lines.append(line)
    if any(re.match(r"Q\d+:", line) for line in lines):
        return ";".join(part for line in lines for part in line.split(";") if part)
    return "".join(lines)


def load_keys():
    with KEYS.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        if next(reader, None) != ["題目ID", "答案", "來源檔"]:
            raise ValueError("expected 題目ID/答案/來源檔 key header")
        keys = {}
        for n, row in enumerate(reader, 2):
            if len(row) != 3 or not row[0] or row[0] in keys:
                raise ValueError(f"invalid or duplicate key row {n}")
            keys[row[0]] = normalize(row[1])
        return keys


def lint(qid, keys):
    path = ADIR / f"{qid}.md"
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return [f"cannot read answer: {exc}"]
    errors = []
    source = MARKERS.get(lines[0] if lines else "")
    if source is None:
        errors.append("L1: expected exact official, drive, or devin src marker")
    body = normalize("\n".join(lines[1:]))
    if not body:
        errors.append("empty answer body")
    if qid in keys:
        if source != "official":
            errors.append("official key exists: src must be official")
        if body != keys[qid]:
            errors.append(f"answer differs from official key: expected {keys[qid]}")
    elif source == "official":
        errors.append("src official requires an entry in keys-交大.tsv")
    option_only = bool(re.fullmatch(
        r"(?:Q\d+:)?\([A-Za-z]+\)(?:\([A-Za-z]+\)|或|均給分|;|,|Q\d+:)*", body
    ))
    if body and (source == "official" or option_only):
        if not re.fullmatch(rf"(?:{CHOICE}|{GROUPED})", body):
            errors.append("invalid multiple-choice format: use uppercase (X) groups, 或 alternatives, or 均給分")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="also report missing in-scope _a files")
    parser.add_argument("ids", nargs="*")
    args = parser.parse_args(argv)
    try:
        keys = load_keys()
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print(f"ERROR keys-交大.tsv {exc}")
        return 1
    ids = sorted(set(args.ids)) if args.ids else sorted(p.stem for p in ADIR.glob("*.md"))
    errors = 0
    for qid in ids:
        for error in lint(qid, keys):
            print(f"ERROR {qid} {error}")
            errors += 1
    if args.all:
        for path in sorted(QDIR.glob("*.md")):
            if not path.stem.startswith("es36121-") and not (ADIR / path.name).is_file():
                if path.stem not in ids:
                    print(f"ERROR {path.stem} missing answer file")
                    errors += 1
    print(f"{len(ids)} checked, {errors} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
