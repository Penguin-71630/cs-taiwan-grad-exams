"""Split a transcription bundle into per-question Markdown files.

Bundle format: sections start with a line `=== <question_id>`; everything until the next
`===` line is that question's Markdown. Usage: python split_bundle.py BUNDLE SRC_DIR
Every id in SRC_DIR/manifest.json must appear exactly once, and no extra ids are allowed.
"""
import json, re, sys
from pathlib import Path

bundle, src = Path(sys.argv[1]), Path(sys.argv[2])
man = json.loads((src / "manifest.json").read_text())
want = {q["id"] for q in man["questions"]}
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
extra, missing = set(parts) - want, want - set(parts)
if extra or missing:
    raise SystemExit(f"extra={sorted(extra)} missing={sorted(missing)}")
for qid, text in parts.items():
    (src / f"{qid}.md").write_text(text)
print(f"wrote {len(parts)} transcriptions to {src}")
