"""Turn the question/unit indexes into one manifest per topic, and report progress.

_src/_index/q-<subject>.tsv      id|year|school|paper|qnum|unit;unit;...   (from build_practice_set)
_src/_index/units-<subject>.tsv  unit_key<TAB>chapter                         (from get_subject_overview)

Usage:
  python plan.py write            (re)write every manifest.json for the subjects that have indexes
  python plan.py status [GROUP]   per-topic count of questions still missing a transcription
  python plan.py todo GROUP N     ids of up to N untranscribed questions, in topic order
"""
import json, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IDX = ROOT / "_src" / "_index"
QDIR = ROOT / "_src" / "_q"
GROUP = {"作業系統": "計系", "計算機組織": "計系", "資料結構": "資演", "演算法": "資演",
         "離散數學": "數學", "線性代數": "數學", "其他": "英文"}
SCHOOL_ORDER = {"台大": 0, "清大": 1, "交大": 2}


def clean(s):
    return " ".join(s.replace("/", "／").split())


def topic_name(unit_key):
    t = unit_key.split("§", 1)[-1]
    t = re.sub(r"^\d+(-\d+)?(~\d+(-\d+)?)?\s+", "", t).strip().rstrip(",").strip()
    return clean(t)


def load():
    topics = {}  # (group, chapter, topic) -> manifest
    for qf in sorted(IDX.glob("q-*.tsv")):
        subject = qf.stem[2:]
        uf = IDX / f"units-{subject}.tsv"
        if not uf.exists():
            continue
        unit_ch = dict(l.rstrip("\n").split("\t") for l in uf.read_text().splitlines() if l.strip())
        group = GROUP[subject]
        for ln in qf.read_text().splitlines():
            if not ln.strip():
                continue
            qid, year, school, paper, qnum, units = ln.split("|", 5)
            for u in units.split(";"):
                if u not in unit_ch:
                    continue
                chapter = clean(unit_ch[u])
                key = (group, chapter, topic_name(u))
                m = topics.setdefault(key, {"unit_key": u, "subject": subject, "group": group,
                                            "chapter": chapter, "topic": key[2], "questions": []})
                if m["unit_key"] != u:  # same chapter/topic name from two subjects
                    key = (group, chapter, f"{key[2]} ({subject})")
                    m = topics.setdefault(key, {"unit_key": u, "subject": subject, "group": group,
                                                "chapter": chapter, "topic": key[2], "questions": []})
                if all(q["id"] != qid for q in m["questions"]):
                    m["questions"].append({"id": qid, "year": int(year), "school": school, "paper": paper,
                                           "qnum": qnum, "url": f"https://img.ptsfu.org/{qid}.webp"})
    return topics


def unit_order(u):
    return [int(x) for x in re.findall(r"\d+", u.split("§", 1)[-1])[:2]] or [999]


def src_dir(m):
    return ROOT / "_src" / m["group"] / m["chapter"] / f"{m['chapter']} - {m['topic']}"


def main():
    cmd = sys.argv[1]
    topics = load()
    ordered = sorted(topics.values(), key=lambda m: (m["group"], m["subject"], unit_order(m["unit_key"]), m["unit_key"]))
    if cmd == "write":
        for m in ordered:
            d = src_dir(m)
            d.mkdir(parents=True, exist_ok=True)
            (d / "manifest.json").write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n")
        print(f"wrote {len(ordered)} manifests")
    elif cmd == "status":
        g = sys.argv[2] if len(sys.argv) > 2 else None
        tot = miss = 0
        for m in ordered:
            if g and m["group"] != g:
                continue
            n = len(m["questions"])
            k = sum(not (QDIR / f"{q['id']}.md").exists() for q in m["questions"])
            tot += n; miss += k
            print(f"{'DONE' if k == 0 else f'{k:>4}'} /{n:>3}  {m['group']}/{m['chapter']}/{m['chapter']} - {m['topic']}")
        print(f"missing {miss} of {tot} question slots")
    elif cmd == "todo":
        g, n = sys.argv[2], int(sys.argv[3])
        out, seen = [], set()
        for m in ordered:
            if m["group"] != g:
                continue
            for q in m["questions"]:
                if q["id"] not in seen and not (QDIR / f"{q['id']}.md").exists():
                    seen.add(q["id"]); out.append(q["id"])
        print(" ".join(out[:n]))


if __name__ == "__main__":
    main()
