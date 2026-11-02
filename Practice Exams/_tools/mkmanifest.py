"""Create a topic source folder + manifest.json from build_practice_set output.

Usage: python mkmanifest.py GROUP CHAPTER UNIT_KEY SUBJECT < rows
rows: one question per line: id|year|school|paper_subject|question_number
(image url is the manifest's image.url, which is always https://img.ptsfu.org/<id>.webp; the
download step fails loudly if that ever stops being true).
Prints the created folder path.
"""
import json, re, sys
from pathlib import Path

def topic_name(unit_key):
    t = re.sub(r"^\d+(-\d+)?(~\d+(-\d+)?)?\s+", "", unit_key).strip().rstrip(",").strip()
    return t.replace("/", "／")

group, chapter, unit_key, subject = sys.argv[1:5]
chapter = " ".join(chapter.split())
topic = topic_name(unit_key)
qs = []
for ln in sys.stdin:
    ln = ln.strip()
    if not ln:
        continue
    qid, year, school, paper, qnum = [x.strip() for x in ln.split("|")]
    qs.append({"id": qid, "year": int(year), "school": school, "paper": paper, "qnum": qnum,
               "url": f"https://img.ptsfu.org/{qid}.webp"})
root = Path(__file__).resolve().parent.parent
d = root / "_src" / group / chapter.replace("/", "／") / f"{chapter.replace('/', '／')} - {topic}"
d.mkdir(parents=True, exist_ok=True)
man = {"unit_key": unit_key, "subject": subject, "group": group, "chapter": chapter, "topic": topic, "questions": qs}
(d / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n")
print(d)
