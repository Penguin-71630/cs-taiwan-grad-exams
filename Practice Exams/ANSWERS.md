# 解答本：交接與計畫

給接手的 session：先讀完這份，再讀 `_tools/ANSWER.md`（child 的作業規格）和 `README.md`。

## 目標（Gino 已決定）

- 每本 Tier 題本各配一本**解答本**，另外成冊：`{類別} - Tier {n} 解答.pdf`，例如 `計系 - Tier 1 解答.pdf`。題本本身不改。
- **只寫答案**，不寫詳解。Gino 卡住時會自己去問其他 AI。
  - 選擇題：選項，例如 `(B)`、`(A)(C)(D)`。
  - 計算、填充：最後的數值或式子。小題逐一列出，例如 `(a) 12 (b) O(n log n)`。
  - 證明題：一行關鍵想法（≤ 1 行），或寫「證明略」。
  - 畫圖、寫程式、描述題：一兩行重點，例如最後的樹寫成括號表示、Gantt chart 寫成順序，程式寫核心那一行。
- 範圍：計系、資演、數學的全部題目，共 1,053 個不重複題目 ID（`_src/_q/*.md` 扣掉英文 `es36121-*`）。英文不做。

## 解答存哪裡

- 每題一個 `_src/_a/<題目ID>.md`，跟 `_src/_q/<ID>.md` 一對一。格式見 `_tools/ANSWER.md`。
- 第一行寫來源標記 `<!-- src: official | drive | devin -->`，解答本會印成小字【官】【詳】【自】，讓 Gino 知道哪些答案比較可信：
  - `official`：學校公布的標準答案（交大 100–106 的選擇題答案 xls，以及 105、106 年的疑義處理結果）。
  - `drive`：Drive 裡的手寫詳解、補習班詳解或網友討論，而且 child 看過、同意這個答案。
  - `devin`：自己解的。
- 沒把握，或來源之間互相矛盾，就寫 `[?]` 加一句原因，不要硬寫。

## 解答來源：Gino 的 Drive 資料夾

- 根目錄 `https://drive.google.com/drive/folders/1lFbUyN3DJNobkVkduWtsPNQFLYPItQ-p`（公開，不用登入）。
- 交大、台大、清大的完整檔案清單在 `_src/_index/drive-answers.tsv`（`路徑<TAB>檔案ID`），是用 `_tools/drive_ls.py` 產生的。下載用 `python3 -m gdown <檔案ID> -O <檔名>`（要先 `pip install gdown xlrd openpyxl`）。
- 100–107 年大致有這些：
  - **交大**：100–106 年選擇題官方答案（xls，104 年有 xlsx），105、106 年的疑義處理結果 PDF。101–104 年的數學（離散、線代）有手寫解答照片。104 年有部分計組解答。
  - **台大**：100–104 年數學（線代、離散）有手寫照片；100 年軟體／OS 有照片；107 年數學有解答 PDF；104 年有網友討論（docx）。
  - **清大**：100–104 年離散有照片；100、104 年計組有照片；104、106、107 年有網友討論（docx）。
  - 其餘，尤其計系、資演的非選題，大多沒有解答，要自己解。
- 交大答案 xls 的格式（以 `交大100數學.xls` 為例）：一個工作表，前幾列是標題（「(1002)-線性代數與離散數學　標準答案表　總題數：10」），接著是「題號｜答案」，答案寫成 `CE`、`ACE` 這樣不加括號。xls 裡的題號是**卷上的題號**。要對照 `_src/_index/q-*.tsv` 的 `題號` 欄，才能找到題目 ID。

## 流程（建議）

1. **Lead 先做（正確性關鍵，不要交給 child）**
   - 把交大官方答案 xls 和疑義處理結果整理成 `_src/_index/keys-交大.tsv`（`題目ID<TAB>答案<TAB>來源檔`）。疑義處理有改答案的，以改過的為準。對不上題號的，列出來人工確認。
   - 照卷別（年、校、卷名）分批，每批約 25 題，同一份考卷盡量放同一批，這樣 Drive 的詳解只要下載一次。每批附上：題目 ID、該卷在 `drive-answers.tsv` 裡相關的檔案 ID，以及 `keys-交大.tsv` 裡的官方答案。
2. **先試跑一批**：約 20 題，計系、資演、數學混合，其中要有官方答案可以比對的題目。用 normal 模式（之前轉錄試過，lite 品質太差）。看完品質再全面展開。
3. **全面展開**：dynamic workflow，大約 40 個 normal child，每個約 25 題，題目 ID 不重疊。child 只寫 `_src/_a/<ID>.md`，照 `_tools/ANSWER.md` 執行，各自 push 一個分支。轉錄時 25 個 child 大約 11 分鐘跑完，寫解答會比較久。
4. **Lead 合併與檢查**
   - 每個題目 ID 都要有 `_a` 檔；跑 `lint_a.py`（新工具，見下方）。
   - 有官方答案的題目，`_a` 一定要跟官方答案一致。
   - 抽查 `devin` 來源的答案，尤其數值題。child 數值題應該已經用 Python 驗算過。
   - 把 `[?]` 的題目列進 `report.md`。
5. **出解答本** `_tools/answers.py`（新工具）：讀 `_tools/tiers.py --out <dir>` 產生的 `tiers.json`，照 Tier 題本裡主題 PDF 的順序排；每個主題一個小標，接著列「第 n 題（104 交大《資料結構與演算法》Q12）【官】 答案」。
   - **題號一定要跟題本一致**：每份主題 PDF 的題號都從 1 開始；有 sections 的合併主題要跳過已經印過的重複題（「另見」）。不要另外重寫一套編號，先把 `build.py` 裡 `build()` 決定題號的邏輯抽成共用函式（例如 `numbering(manifest) -> [(n, question, section_topic)]`），`build.py` 和 `answers.py` 都用這個函式。`build.py` 重構後，`check.py` 必須 0 失敗，而且 PDF 文字要跟重構前完全一樣。
   - 版面比照題本，盡量省紙：A4、雙欄、9 pt，題目和題目之間不留空白。
   - 解答本跟 Tier 題本一樣是本地產物，**不放進 repo**。用附件傳給 Gino。程式碼、`_a/*.md`、`keys-交大.tsv` 要進 repo，透過 PR 送出，不要直接 merge。

## 需要新寫的工具

- `_tools/ANSWER.md`：child 規格（已寫好）。
- `_tools/lint_a.py`：檢查 `_a` 檔：第一行的 src 標記合法；內容不是空的；`official` 的答案跟 `keys-交大.tsv` 一致；選擇題答案的格式是 `(X)` 的組合。
- `_tools/answers.py`：產生解答本（見上面第 5 步）。

## 環境

跟 `README.md` 的「環境需求」相同：pandoc 3.1.3、`typst==0.13.2`、字型，先 `export TIKU_FONTS=$HOME/fonts`。另外需要 `pip install gdown xlrd openpyxl pypdf`，網路要能連 `drive.google.com`、`drive.usercontent.google.com`。
Tier 題本用 `python3 _tools/tiers.py --out ~/tiers/out` 產生，分級規則和 Gino 指定要升級的子主題在 `_src/_index/tier-promote.json`。
