"""Verify every built PDF against its manifest and write Practice Exams/report.md.

For each _src/<group>/<chapter>/<topic>/manifest.json:
  - the PDF exists at <group>/<chapter>/<topic>.pdf
  - the PDF's question headers 第 1 題 … 第 N 題 match the manifest count
  - every question id from the manifest is printed in the PDF
  - transcriptions containing [?] are listed
Usage: python check.py            (exit code 1 if any check fails)
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def pdf_text(pdf):
    return subprocess.run(["pdftotext", "-raw", str(pdf), "-"], capture_output=True, text=True, check=True).stdout


def question_headers(text, questions):
    qids = [q["id"] for q in questions]
    heads = set()
    for line in text.splitlines():
        m = re.match(r"^[ \t]*第\s*(\d+)\s*題", line)
        if m and any(line.rstrip().endswith(qid) for qid in qids):
            heads.add(int(m.group(1)))
    return heads


def pages(pdf):
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))


def main():
    rows, unclear, failures, corrected = [], [], [], []
    for man_path in sorted(p for p in (ROOT / "_src").glob("*/*/*/manifest.json") if not p.parts[-4].startswith("_")):
        src = man_path.parent
        man = json.loads(man_path.read_text())
        rel = src.relative_to(ROOT / "_src")
        pdf = ROOT / rel.parent / f"{src.name}.pdf"
        n = len(man["questions"])
        status, npages = "OK", "-"
        if not pdf.exists():
            status = "PDF 不存在"
        else:
            txt = pdf_text(pdf)
            npages = pages(pdf)
            heads = question_headers(txt, man["questions"])
            missing_ids = [q["id"] for q in man["questions"] if q["id"] not in txt.replace("\n", "")]
            if heads != set(range(1, n + 1)):
                status = f"題號不符：PDF {len(heads)} 題 / manifest {n} 題"
            elif missing_ids:
                status = f"缺少題目 ID：{', '.join(missing_ids)}"
        if status != "OK":
            failures.append(f"{rel}: {status}")
        qdir = ROOT / "_src" / "_q"
        skew = json.loads((qdir / "deskew.json").read_text()) if (qdir / "deskew.json").exists() else {}
        for q in man["questions"]:
            md = qdir / f"{q['id']}.md"
            if md.exists() and "[?]" in md.read_text():
                unclear.append((rel, q))
            if skew.get(q["id"], {}).get("corrected") and md.exists() and "<!-- fig" in md.read_text():
                corrected.append((rel, q, skew[q["id"]]["angle"]))
        rows.append((man["group"], man["chapter"], src.name, n, npages, status))

    lines = ["# Practice Exams 題本報告", "",
             "範圍：台大、交大、清大，民國 100–107 年。題目來源為考古題題庫 MCP（`build_practice_set` + `include_manifest`），"
             "原圖由 `image_url` 下載；轉錄稿逐張看原圖手打，不使用題庫摘要文字。", "",
             f"共 {len(rows)} 份 PDF、{sum(r[3] for r in rows)} 題（同一題可能屬於多個單元而重複出現）。", "",
             "## 各主題題數", "", "| 類別 | 大類 | 主題 | 題數 | 頁數 | 檢查 |", "|---|---|---|---:|---:|---|"]
    for g, c, t, n, p, s in rows:
        lines.append(f"| {g} | {c} | {t} | {n} | {p} | {s} |")
    lines += ["", "## 含 [?] 的題目", ""]
    if unclear:
        for rel, q in unclear:
            lines.append(f"- {rel}：{q['year']} {q['school']}《{q['paper']}》{q['qnum']}（`{q['id']}`）")
    else:
        lines.append("無。")
    lines += ["", "## 已校正歪斜的原圖（只有需要裁切圖表的題目會用到原圖）", "",
              "門檻 0.75°（只校正明顯歪斜的圖）；原檔保留於快取 `orig/`，校正後另存 `fixed/`。", ""]
    if corrected:
        for rel, q, a in corrected:
            lines.append(f"- {rel}：{q['year']} {q['school']} {q['qnum']}（`{q['id']}`），{a:+.1f}°")
    else:
        lines.append("無。")
    lines += ["", "## 失敗項目", ""]
    lines += [f"- {f}" for f in failures] or ["無。"]
    (ROOT / "report.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
