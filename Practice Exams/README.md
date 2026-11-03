# Practice Exams

台大、交大、清大資工所考古題的分主題 PDF 題本，範圍是民國 100–107 年（108 年之後留作模考，不收錄）。

```
Practice Exams/
├── 計系/{大類}/{大類} - {主題}.pdf     計算機組織、作業系統（Times New Roman）
├── 資演/{大類}/{大類} - {主題}.pdf     資料結構、演算法（Computer Modern）
├── 數學/{大類}/{大類} - {主題}.pdf     離散數學、線性代數（Computer Modern）
├── 英文/…                              只有台大考，科目在題庫叫「其他」（Times New Roman）
├── report.md                           題數、[?] 題目、校正過的圖、失敗項目
├── _src/_index/                        題目與單元索引（見下方「交接」）
├── _src/_q/<題目ID>.md                 每題一份轉錄稿；同一題出現在多個主題時共用
├── _src/{類別}/{大類}/{大類} - {主題}/manifest.json   每個主題的題目清單（由 plan.py 產生）
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

## 交接：目前進度與接手步驟（2026-11-02）

| 類別 | 科目 | 狀態 |
|---|---|---|
| 計系 | 作業系統、計算機組織 | 索引完成；986 個「主題×題目」中已轉錄 885 個（還差 101），完成的主題都已出 PDF |
| 資演 | 資料結構、演算法 | 只做了試跑的 Master Method。`units-資料結構.tsv` 已完成（105 個單元）；題目索引只抓了前 3 頁共 150 題，存成 `q-資料結構.tsv.partial`（副檔名不是 .tsv，所以 plan.py 不會讀它）。演算法索引還沒建 |
| 數學 | 離散數學、線性代數 | 只做了試跑的 Cayley-Hamilton；索引還沒建 |
| 英文 | 其他（只有台大） | 還沒開始 |

`python3 _tools/plan.py status` 會列出每個主題還缺幾題。

### 環境需求

`pandoc`（3.1）、`pdftotext`／`pdfinfo`（poppler）、Python 套件 `typst==0.13.2`、`pillow`、`numpy`；
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
- 選項每行結尾用 `\` 換行；程式碼用 ``` 區塊；表格用 Markdown 表格。原卷明顯印錯的地方照抄，再用 `> 註：…` 說明。
- 圖表用 `<!-- fig x0 y0 x1 y1 -->` 嵌入原圖裁切，座標是原圖（校正後）寬高的比例。
  montage 的 sheet 會把寬於 1600 px 的圖縮小，而且太高的圖會切成多段（每段往下 1906 px），換算座標時要考慮這兩點。
  裁完最好把裁切結果開來看一次。
- 歪斜 ≥ 0.75° 的圖會自動校正（`deskew.py`），校正角度記在 `_src/_q/deskew.json`。

改了 `_tools/build.py` 之後，publish.py 會把所有主題重排一次（約 30 秒）。

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
