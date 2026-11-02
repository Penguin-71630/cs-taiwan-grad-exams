"""Split a transcription bundle into per-question Markdown files in _src/_q/.

Bundle format: sections start with a line `=== <question_id>`; everything until the next
`===` line is that question's Markdown. Usage: python split_bundle.py BUNDLE [--force]
Existing transcriptions are not overwritten unless --force is given.
"""
import re, sys
from pathlib import Path

QDIR = Path(__file__).resolve().parent.parent / "_src" / "_q"
bundle = Path(sys.argv[1])
force = "--force" in sys.argv
parts, cur, buf = {}, None, []
for ln in bundle.read_text().split("\n"):
    m = re.match(r"^=== ([a-z0-9_]+)\s*$", ln)
    if m:
        if cur:
            parts[cur] = "\n".join(buf).strip() + "\n"
        cur, buf = m.group(1), []
        if cur in parts:
            raise SystemExit(f"duplicate id {cur}")
    else:
        buf.append(ln)
if cur:
    parts[cur] = "\n".join(buf).strip() + "\n"
QDIR.mkdir(parents=True, exist_ok=True)
skipped = []
for qid, text in parts.items():
    f = QDIR / f"{qid}.md"
    if f.exists() and not force:
        skipped.append(qid)
        continue
    f.write_text(text)
print(f"wrote {len(parts) - len(skipped)} transcriptions" + (f", skipped existing: {skipped}" if skipped else ""))
