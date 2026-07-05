# UCB CS61C Fall 2020 — Labs & Projects 摘要

> 版本：Fall 2020  
> Starter code: https://github.com/61c-teach/fa20-lab-starter  
> Lab spec 全文：https://www.learncs.site/docs/curriculum-resource/cs61c/labs/  
> Project spec 全文：https://www.learncs.site/docs/curriculum-resource/cs61c/projects/

---

## Labs

### Lab 0 — Setup & Git

**做什麼：** 設定開發環境（GitHub、Gradescope、Hive SSH）、學習 Linux 指令與 Git 基本操作。  
**學到什麼：** 熟悉課程工具鏈與 Git 版本控制的基礎流程（clone、commit、push）。

---

### Lab 1 — C Programming & GDB Debugging

**做什麼：**
- Exercise 1：操控 `#define` 巨集控制 C 程式的 control flow（if/else、switch、for、ternary）產生指定輸出。
- Exercise 2：用 GDB/CGDB 設定 breakpoint、單步執行、印出變數值，除錯一個簡單 C 程式。
- Exercise 3：用 bitwise operators 實作一個 regex pattern matcher。

**學到什麼：** C 語言控制流程、preprocessor macro、GDB 偵錯技巧（breakpoint、step、next、print、display）、stdin redirection。

---

### Lab 2 — Bit Operations, LFSR & Memory Management

**做什麼：**
- Exercise 0：閱讀 Makefile 結構、回答 Make 相關問題。
- Exercise 1：實作 `get_bit`、`set_bit`、`flip_bit`（只能用 bitwise ops，禁止 branch/loop）。
- Exercise 2：實作 16-bit Linear Feedback Shift Register（XOR tap positions 0, 2, 3, 5），驗證能產生全部 65535 個非零正整數。
- Exercise 3：實作 variable-length array（`vector_new`、`vector_get`、`vector_set`、`vector_delete`），用 Valgrind 檢查 memory leak。

**學到什麼：** Makefile 使用、bitwise 操作技巧、LFSR 偽隨機數產生原理、C 動態記憶體管理（malloc/free）、Valgrind memcheck。

---

### Lab 3 — RISC-V Assembly & Venus Simulator

**做什麼：**
- Exercise 0：在 Venus 模擬器中掛載本地檔案系統。
- Exercise 1：逐步執行 RISC-V 程式（Fibonacci），觀察暫存器與記憶體狀態。
- Exercise 2：閱讀 C → RISC-V 翻譯範例，辨認變數、指標、迴圈對應的組語結構。
- Exercise 3：自行實作 `factorial` 函式（遞迴或迴圈）。
- Exercise 4：使用 Venus 的 Calling Convention Checker（`-cc` flag）驗證函式呼叫規範。

**學到什麼：** RISC-V 指令集入門（`.data`/`.text` 指令）、Venus 模擬器操作、C 到 RISC-V 的翻譯思維、函式呼叫慣例（caller/callee saved registers）。

---

### Lab 4 — RISC-V Linked List & Calling Convention

**做什麼：**
- Exercise 1：除錯 `megalistmanips.s`——一個在 linked list of int arrays 上做 `map` 的遞迴函式。找出 5 個 bug（stack save/restore 錯誤、load vs. move 混淆、struct offset 錯誤等），修正後通過 CC checker。
- Exercise 2：實作 `discrete_fn.s`——不使用任何 branch/jump 指令實作離散查表函式（利用 base + offset 動態 load）。

**學到什麼：** RISC-V calling convention 的實際除錯經驗、struct 在記憶體中的 layout、pointer chasing in assembly、branchless programming（用 load word from computed address 取代 if-else）。

---

### Lab 5 — Digital Logic with Logisim (Combinational + FSM)

**做什麼：**
- Part 1：用 AND、OR、NOT 組合出 NAND、NOR、XOR、2-to-1 MUX、4-to-1 MUX sub-circuits。
- Part 2：用 register + adder 建造一個 8-bit counter（每 clock cycle +1），熟悉 stateful circuit。
- Part 3：將 FSM（有限狀態機）轉換成 Logisim 數位邏輯電路——用 register 存 state，combinational logic 算 next-state 和 output。

**學到什麼：** Logisim Evolution 操作、從 truth table 設計 combinational logic、register 的 CLK-to-Q/setup/hold time 觀念、FSM → digital circuit 的轉換方法。

---

### Lab 6 — Pipelining & Timing Analysis

**做什麼：**
- Exercise 1：分析一個 non-pipelined 電路（multiplier + adder + register）的 critical path，計算最大 clock rate。
- Exercise 2：將該電路切成兩級 pipeline（multiplication stage → addition stage），加入 pipeline register，重新計算最大 clock rate；解釋為何此電路不需要 pipeline bubble。

**學到什麼：** Critical path 分析（propagation delay、CLK-to-Q、setup time）、pipeline 的基本概念與實作、為何 pipeline 可以提高 throughput、何時需要/不需要 bubble。

---

### Lab 7 — Caches

**做什麼：**
- 使用 Venus 的 Cache Simulator 模擬不同 cache 配置（direct-mapped、N-way set associative）下的 hit/miss 行為。
- 設定 Array Size、Step Size、Rep Count、Option 等參數，觀察 hit rate 變化。
- 分析 write-through/write-back、write-allocate/no-write-allocate 策略。
- 手動推導為何特定 access pattern 會造成特定 hit/miss pattern，並提出優化方案。

**學到什麼：** Cache 的 tag/index/offset 分解、direct-mapped vs. set-associative 的行為差異、LRU 替換策略、write policy（write-through vs. write-back）、如何從 access pattern 預測 hit rate、spatial/temporal locality 概念。

---

### Lab 8 — Virtual Memory (TLB & Page Table)

**做什麼：**
- 使用 CAMERA 模擬器視覺化 virtual memory 系統（TLB + Page Table + Physical Memory）。
- 觀察 address reference string 下的 TLB hit/miss 與 Page Fault 行為。
- 設計一組 10 個 address 造成 10 次 TLB miss + 10 次 Page Fault。
- 調整系統參數（TLB size、Physical Memory size、Page size）觀察對 fault rate 的影響。
- 使用 VMSIM 觀察多進程環境下的 TLB miss 比例升高原因。

**學到什麼：** Virtual address → Physical address 翻譯流程、TLB 的作用與 hit/miss 判定、Page Table 查詢與 Page Fault 處理、VPN/PPN bit 數的意義、多進程 context switch 對 TLB 的衝擊。

---

### Lab 9 — SIMD (Data-Level Parallelism)

**做什麼：**
- Exercise 1：查閱 Intel Intrinsics Guide，找到 SSE 128-bit 指令（float division、int8 max、int16 arithmetic shift right）。
- Exercise 2：將 naive `sum()` 函式用 SSE intrinsics（`_mm_loadu_si128`、`_mm_add_epi32`、`_mm_cmpgt_epi32`、`_mm_and_si128`）向量化成 `sum_simd()`，達到約 4-7x 加速。
- Exercise 3：在 SIMD 版本上再做 loop unrolling（展開 4 次），進一步減少 loop overhead。

**學到什麼：** SIMD/SSE 程式設計實務、128-bit vector 操作（load、store、add、compare、mask）、conditional sum 的向量化技巧、loop unrolling 原理與加速效果、memory alignment 注意事項。

---

### Lab 10 — Thread-Level Parallelism (OpenMP) & Multi-Processing

**做什麼：**
- Exercise 1：OpenMP Hello World（`#pragma omp parallel`），觀察 thread ID 亂序輸出。
- Exercise 2：實作向量加法的兩種平行化方式——slicing（thread i 處理 index % N == i 的元素）和 chunking（每個 thread 處理連續一段），比較效能差異（false sharing）。
- Exercise 3：實作平行 dot product——先用 `#pragma omp critical` 的 naive 版本（觀察 contention 問題），再用手動 local sum + 最後 reduce，最後用 `#pragma omp reduction` 關鍵字。
- Part 2：用 `fork()` 實作 multi-process HTTP web server，理解 process vs. thread 的差異。

**學到什麼：** OpenMP 基本語法（`parallel`、`for`、`critical`、`reduction`）、false sharing 問題與 chunking 解決方案、data race 與 critical section、multi-processing（fork）vs. multi-threading 的差異與取捨。

---

### Lab 11 — Spark / MapReduce

**做什麼：**
- Exercise 0：用 Hadoop Importer 將文本檔轉為 Spark `.seq` 格式。
- Exercise 1：執行提供的 `wordCount.py`（MapReduce word count）。
- Exercise 2：修改程式計算「每個 word 出現在幾個 document 中」（per-word document count），輸出按字母排序。
- Exercise 3：建立 Full Text Index（對每個 word，列出它在每個 document 中的所有出現位置）。

**學到什麼：** MapReduce 計算模型（map → shuffle → reduce）、Apache Spark Python API（`map`、`flatMap`、`reduceByKey`、`sortByKey`）、request-level parallelism 概念、分散式計算的基本思維。

---

## Projects

### Project 1 — Conway's Game of Life, in RGB!

**做什麼：**
- 用 C 實作 Conway's Game of Life 的 RGB 彩色版本。
- Part A：實作 PPM 影像檔 I/O（讀取/寫入 P3 格式）、在 `Image` struct 上操作像素。
- Part B：實作 Game of Life 規則——每個 color channel (R, G, B) 獨立演化，alive/dead 取決於 8 鄰居中同 channel alive 的數量（standard rules: 2-3 survive, 3 birth）。支援 toroidal wrap-around 邊界。

**學到什麼：** C 語言 file I/O（`fopen`/`fscanf`/`fprintf`）、struct 與 2D array 操作、pointer 與動態記憶體配置、模組化程式設計（header + implementation 分離）、影像處理基礎。

---

### Project 2 — CS61Classify (RISC-V Neural Network)

**做什麼：**
- 用純 RISC-V 組語實作一個手寫數字辨識的 Artificial Neural Network。
- Part A：實作基本矩陣運算——`dot product`（含 stride）、`matmul`（矩陣乘法）、`argmax`、`ReLU` activation function。
- Part B：實作二進制矩陣檔案的讀取/寫入（`read_matrix`、`write_matrix`），然後將所有函式串接起來完成 MNIST 分類器的 forward pass（兩層全連接 + ReLU + argmax）。

**學到什麼：** 大規模 RISC-V 組語開發經驗、calling convention 的嚴格遵守（prologue/epilogue、s-registers save/restore）、用 assembly 操作 file I/O（ecall）、矩陣在記憶體中的 row-major layout、neural network inference 的底層實作。

---

### Project 3 — CS61CPU (Pipelined RISC-V CPU in Logisim)

**做什麼：**
- 在 Logisim Evolution 中從零搭建一個 RISC-V CPU。
- Part A（Tasks 1-3）：建造 ALU（支援 add/sub/and/or/xor/sll/srl/sra/slt/mul）、Register File（32 registers, x0 hardwired to 0）、Immediate Generator，並完成能執行 `addi` 的單週期 datapath。
- Part B（Tasks 4-5）：擴展成完整 pipelined CPU——支援所有 RV32I 指令（R-type、I-type、S-type、B-type、U-type、J-type）、實作 hazard detection + forwarding（data hazards）、branch prediction / flush（control hazards）。

**學到什麼：** CPU datapath 設計的完整流程（instruction fetch → decode → execute → memory → writeback）、control signal 的產生邏輯、pipeline register 的作用、data hazard 的 forwarding 解法、control hazard 的 flush/stall 解法、如何用 Logisim 實作並測試一個真正能跑指令的 CPU。

---

### Project 4 — Numc (High-Performance Matrix Library)

**做什麼：**
- 用 C 實作一個矩陣運算庫（mini-NumPy），並透過 Python-C interface 讓 Python 可以 `import numc`。
- Task 1：實作矩陣基本操作的 naive 版本（allocate/deallocate、get/set、add、sub、mul、pow、neg、abs、fill）。
- Task 2：撰寫 `setup.py` 安裝 Python C extension module。
- Task 3：實作 Python-C interface——overload operators（`+`、`-`、`*`、`**`、negation、abs）、implement `__subscr__`（indexing/slicing）。
- Task 4：效能優化——用 SIMD（SSE/AVX）、OpenMP 多線程、cache blocking（loop tiling）、matrix transpose optimization 將矩陣乘法加速到接近 numpy 效能。

**學到什麼：** C 與 Python 的互操作（CPython C API、`PyObject`、reference counting）、矩陣乘法的效能優化全技巧組合（SIMD + OpenMP + cache blocking + loop unrolling）、memory access pattern 對 cache performance 的影響、如何量測與分析程式效能瓶頸。
