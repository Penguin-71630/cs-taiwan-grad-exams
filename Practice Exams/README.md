# Practice Exams

台大、交大、清大資工所考古題的分主題 PDF 題本，範圍是民國 100–107 年（108 年之後留作模考，不收錄）。

```
Practice Exams/
├── 計系/{大類}/{大類} - {主題}.pdf     計算機組織、作業系統（Times New Roman）
├── 資演/{大類}/{大類} - {主題}.pdf     資料結構、演算法（Computer Modern）
├── 數學/{大類}/{大類} - {主題}.pdf     離散數學、線性代數（Computer Modern）
├── report.md                           題數、[?] 題目、校正過的圖、失敗項目
├── _src/…/{大類} - {主題}/              manifest.json、每題的轉錄稿 <題目ID>.md、deskew.json
└── _tools/                             產生題本的程式
```

## 每題的內容

- **出處**：年度、學校、卷名、題號（加上題庫的題目 ID，方便回查）
- **轉錄文字**：逐張看原圖手打的 Markdown + LaTeX，不使用題庫的摘要文字。看不清楚的地方標紅色 **[?]**，不猜
- **圖表**：不附整張原圖；題目有圖表時，從原圖裁切出圖表那一塊嵌入，不重畫（轉錄稿裡寫成 `<!-- fig x0 y0 x1 y1 -->`）。只校正明顯歪斜（≥ 0.75°）的圖
- **空白**：每題後面留約 4 行空白，給作答和計算用

程式碼不加底色，方便列印。

字型：中文一律 Noto Serif TC，程式碼用 DejaVu Sans Mono，數學式用 New Computer Modern Math。
「Computer Modern」用的是 New Computer Modern，也就是 LaTeX 預設字型 Computer Modern 的 OpenType 版本。

## 重建方式

需要 `pandoc`、`pdftotext`／`pdfinfo`（poppler）、Python 套件 `typst==0.13.2`、`pillow`、`numpy`，
以及放在 `/root/fonts`（或環境變數 `TIKU_FONTS`）的 Times New Roman、Noto Serif TC 字型檔。

```bash
# 1. 由 build_practice_set(include_manifest=true) 的結果建立 manifest（每行 id|年|校|卷名|題號）
python _tools/mkmanifest.py 計系 "Process" "3-3 Process Tree, fork(), wait(), Zombie, Orphan" 作業系統 < rows.txt
# 2. 下載原圖，轉成 PNG 方便看圖轉錄
python _tools/fetch.py "_src/計系/Process/Process - …" view/
# 3. 轉錄稿（=== <id> 分段）拆成各題的 .md
python _tools/split_bundle.py bundle.md "_src/計系/Process/Process - …"
# 4. 排版（Typst）
python _tools/build.py "_src/計系/Process/Process - …" "計系/Process/Process - ….pdf"
# 5. 檢查所有 PDF 的題數與題目 ID 是否和 manifest 一致，並輸出 report.md
python _tools/check.py
```

## 試跑結果（2026-11-02）

先在三個類別各做一個單元，確認 MCP 和圖片下載都可以用：

| 類別 | 單元 | 題數 | 頁數 | 結果 |
|---|---|---:|---:|---|
| 計系 | 作業系統 3-3 Process Tree, fork(), wait(), Zombie, Orphan | 10 | 8 | OK |
| 資演 | 資料結構 1-7 Master Method | 13 | 6 | OK |
| 數學 | 線性代數 5-6 Cayley-Hamilton | 3 | 1 | OK |

- `build_practice_set` 可以正常使用，`img.ptsfu.org` 的原圖也下載得到（要先在雲端環境的 Allowed domains 加上這個網域）。
- 原圖裡會重複出現的頁首「【不可使用計算機】」沒有轉錄；作答規則（單選、複選、倒扣）有保留。
- 102 交大《計算機系統》Q2 的 `runner` 函式，兩個大括號在原圖中印成實心黑色方塊，所以標成 [?]。
- 第一版每題都附整張原圖；確認轉錄品質後改成只放轉錄文字，有圖表的題目才嵌入裁切的圖。
- 手機上看的預覽圖在 `_preview/README.md`。
