# Practice Exams

台大、交大、清大資工所考古題的分主題 PDF 題本，計系、資演、數學收錄民國 100–107 年；英文（A）另收 111 年台大卷，112–115 年留作模考。

```
Practice Exams/
├── 計系/{大類}/{大類} - {主題}.pdf     計算機組織、作業系統（Times New Roman）
├── 資演/{大類}/{大類} - {主題}.pdf     資料結構、演算法（Computer Modern）
├── 數學/{大類}/{大類} - {主題}.pdf     離散數學、線性代數（Computer Modern）
├── 英文/英文（A）/英文（A） - {主題}.pdf  英文（Times New Roman）
├── report.md                           題數、[?] 題目、校正過的圖、失敗項目
├── _src/_index/                        題目與單元索引（見下方「交接」）
├── _src/_q/<題目ID>.md                 每題一份轉錄稿；同一題出現在多個主題時共用
├── _src/{類別}/{大類}/{大類} - {主題}/manifest.json   題目清單（計系／資演／數學由 plan.py 合併產生；英文另行維護）
└── _tools/                             產生題本的程式
```

## 每題的內容

- **出處**：年度、學校、卷名、題號（加上題庫的題目 ID，方便回查）
- **轉錄文字**：逐張看原圖手打的 Markdown + LaTeX，不使用題庫的摘要文字。看不清楚的地方標紅色 **[?]**，不猜
- **圖表**：不附整張原圖；題目有圖表時，從原圖裁切出圖表那一塊嵌入，不重畫（轉錄稿裡寫成 `<!-- fig x0 y0 x1 y1 -->`）。只校正明顯歪斜（≥ 0.75°）的圖
- **空白**：每題後面留約 2 行空白，給作答和計算用
- **英文**：題目後不留作答空白；較短的 (A)–(D) 選項排在同一行
- **版面**：A4，左右邊界 1.5 cm、上下 1.8 cm；內文 10 pt
- **排版**：題目高度不超過 12 cm 時保持在同頁；較長題目可跨頁，題號標頭會黏在題目開頭。

程式碼不加底色，方便列印。

字型：中文一律 Noto Serif TC，程式碼用 DejaVu Sans Mono，數學式用 New Computer Modern Math。
「Computer Modern」用的是 New Computer Modern，也就是 LaTeX 預設字型 Computer Modern 的 OpenType 版本。

## 交接：目前進度與接手步驟（2026-11-03）

| 類別 | 科目 | 狀態 |
|---|---|---|
| 計系 | 作業系統、計算機組織 | 全部轉錄完成，99 個合併主題都已出 PDF |
| 資演 | 資料結構、演算法 | 全部轉錄完成，84 個合併主題都已出 PDF |
| 數學 | 離散數學、線性代數 | 全部轉錄完成，54 個合併主題都已出 PDF |
| 英文 | 英文（A） | 1 個主題：111 年台大碩士班《英文（A）》由 Examshore 原卷影像轉錄；112–115 年保留作模考 |

主題依章節合併：章內不重複題目 ID 聯集 ≤15 時列為「全章」；否則少於 5 題的主題合併為「其他主題」，並以 sections 分段。只有一個小主題時保留原名；重複題只排一次，後續主題以「另見：第 n 題」標示。

`[?]` 題目見 `report.md`。2026-11-03 起的轉錄是平行分批做的：每批約 25 題交給一個獨立 session，
只照 `_tools/TRANSCRIBE.md` 寫 `_src/_q/<ID>.md`（用 `view.py`、`crop_preview.py`、`lint_q.py`，不需排版環境），
各自 push 一個分支，再合併後統一跑 `publish.py`、`check.py`。

`python3 _tools/plan.py status` 會列出每個主題還缺幾題。

### 環境需求

`pandoc`（3.1.3；3.1.13 會把 cases 裡的逗號轉壞）、`pdftotext`／`pdfinfo`（poppler）、Python 套件 `typst==0.13.2`、`pillow`、`numpy`；
字型放在 `/root/fonts`（或環境變數 `TIKU_FONTS`）：Times New Roman（corefonts 的 times32.exe 用 cabextract 解出）、
Noto Serif TC。New Computer Modern 是 typst 內建的。
網路要能連 `img.ptsfu.org`（原圖，下載時要設 User-Agent）、`tiku.ptsfu.org`，push PDF 要能連 `lfs.github.com`（PDF 用 Git LFS）。
原圖快取在 `~/.cache/tiku/`（orig 原圖、fixed 校正後、crop 裁圖、typ 排版中間檔）。

### 1. 建索引（一個科目做一次）

1. `get_subject_overview(subject)` 取得所有單元，寫成 `_src/_index/units-<科目>.tsv`，每行 `unit_key<TAB>大類`。
   大類就是 PDF 的資料夾名稱；計系的對照可以參考既有的兩個 units 檔。
2. `build_practice_set(subject, schools=[台大,交大,清大], years 100–107, count=50, include_manifest=true)`，
   每次把已拿到的 id 放進 `exclude_ids` 重抓，直到回傳數不足 50 為止。
   寫成 `_src/_index/q-<科目>.tsv`，每行 `id|年|校|卷名|題號|單元;單元;…`（單元用 unit_key 去掉「科目§」的部分）。
   - 接續 `q-資料結構.tsv.partial`：把檔案裡的 150 個 id 放進 `exclude_ids` 繼續抓（不加 include_manifest 也有 year、school、paper_subject、question_number、unit_keys；每頁 50 題約 25k tokens），抓到回傳少於 50 題為止，再改名成 `q-資料結構.tsv`。
   - unit_keys 會混入其他科目（如演算法）的單元，照存即可；plan.py 只認 units 檔裡有的單元。
   - 比較省 token 的做法（2026-11-03 建資演、數學索引時用的）：網站的公開索引 `https://tiku.ptsfu.org/index.json.gz`
     有每題的年、校、卷名、題號、單元，`python3 -I _tools/derive_index.py index.json.gz units-<科目>.tsv <科目>` 可以直接產生草稿。
     草稿一定要用 MCP 核對：`build_practice_set(exclude_ids=草稿全部 id)` 必須回傳 0 題（回傳的題目要補進去），
     再排除到只剩約 10 題，回傳的 unit_keys 要和草稿一致。資料結構 259 題逐題比對完全相同；
     離散數學靠這個核對補了 36 題（清大、交大軟體卷裡只有離散單元的題目）。
   - 別科的主科單元（例如數學卷題目上的資料結構單元）MCP 會直接丟掉；程式語言、工程數學、資料庫這類非主科單元則寫成「<科目>§單元」，
     units 檔裡大類寫成那個科目名稱（程式語言、工程數學）。
3. `python3 _tools/plan.py write` 產生各主題的 manifest.json（科目→類別的對照在 plan.py 的 `GROUP`）。

### 2. 轉錄（一批約 12 題）

```bash
python3 _tools/plan.py todo 計系 12                 # 下一批還沒轉錄的題目 ID
python3 _tools/montage.py /tmp/m ID1 ID2 …          # 下載原圖、拼成 sheet-01.png… 方便看；會印出原圖尺寸與縮放比例
# 看圖逐題手打 Markdown + LaTeX，寫成一個 bundle：每題以「=== <題目ID>」開頭
python3 _tools/split_bundle.py bundle.md            # 拆成 _src/_q/<ID>.md（已存在的不覆蓋，加 --force 才覆蓋）
python3 _tools/publish.py                           # 轉錄齊全且過期的主題全部重排、檢查題號與 ID、每主題一個 commit、最後 push
python3 _tools/check.py                             # 更新 report.md
```

轉錄規則：

- 不使用題庫的 text 摘要；看原圖。看不清楚的地方寫 `[?]`，不猜。
- 卷首「【不可使用計算機】」等頁首不轉；作答規則（單選／複選／倒扣、「請詳細列出完整過程」）保留在題目開頭。
- 範圍的波浪號要寫成 `\~`（如 `21\~23`、`P0\~P4`）：單獨的 `~` 在 pandoc 是下標，`build.py` 會把 `\~` 轉成 typst 的 `\~`（typst 的 `~` 是不換行空白）。
- 選項每行結尾用 `\` 換行；程式碼用 ``` 區塊；表格用 Markdown 表格。原卷明顯印錯的地方照抄，再用 `> 註：…` 說明。
- 圖表用 `<!-- fig x0 y0 x1 y1 -->` 嵌入原圖裁切，座標是原圖（校正後）寬高的比例。
  montage 的 sheet 會把寬於 1600 px 的圖縮小，而且太高的圖會切成多段（每段往下 1906 px），換算座標時要考慮這兩點。
  裁完最好把裁切結果開來看一次。
- 歪斜 ≥ 0.75° 的圖會自動校正（`deskew.py`），校正角度記在 `_src/_q/deskew.json`。

改了 `build.py` 要用 `python3 _tools/publish.py --all` 全部重排（否則只重排 manifest／轉錄稿有變的主題）。

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
