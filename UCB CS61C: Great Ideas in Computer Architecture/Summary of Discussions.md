# UCB CS61C Fall 2020 — Discussions 摘要

> 版本：Fall 2020  
> Discussion PDF（含解答）：https://github.com/Chih-EnShen/cs61c-all-materials/tree/main/fa20/discussion  
> 共 14 份 discussion worksheet，每份含 Pre-Check（概念判斷題）+ 手寫練習題 + 解答

---

### Discussion 1 — Number Representation

**主題：** 進制轉換與有號數表示法  
**練習內容：**
- 二進制 / 十進制 / 十六進制互轉（含 IEC prefix：Ki, Mi, Gi...）
- Unsigned、Two's Complement、Biased notation 的表示與比較
- 溢位（overflow）判斷：同號相加結果異號才 overflow
- Two's complement 取反技巧證明（flip all bits + 1）
- 6-bit Two's Complement 加減法手算

**考研相關：** 數字表示法是所有計組題目的基礎，Two's Complement overflow 判斷是常考選擇題。

---

### Discussion 2 — C Basics (Pointers, Memory Management)

**主題：** C 語言指標、記憶體管理、linked list  
**練習內容：**
- 指標解引用鏈（`*pp`、`**pp`）的值追蹤
- 閱讀晦澀 C 函式並用白話描述行為（遞迴 array sum、bitwise NOT 取負、XOR swap）
- 實作 `swap`、`mystrlen`（不用 strlen）
- 找出 C 函式中的 bug（`sizeof(pointer)` 誤用、pointer 宣告遺漏 `*`）
- 記憶體四區段分類（code / static / heap / stack）
- `malloc` 動態配置：int array、string、n×m matrix
- Linked list 操作：`prepend`（為何用 `**lst`）、`free_ll`

**考研相關：** C 指標與記憶體管理是 OS 的前置知識，linked list 操作在資料結構常考。

---

### Discussion 3 — Floating Point (IEEE 754)

**主題：** IEEE 754 單精度浮點數表示  
**練習內容：**
- Sign / Exponent（bias = -127）/ Mantissa 三欄位拆解
- Normalized vs. Denormalized vs. Infinity vs. NaN 的判斷
- 最大有限正值、最小正值、最小正 normalized 值的計算
- 十進制 ↔ 二進制浮點數互轉（如 8.25、39.5625）
- Step size（相鄰可表示數的間距）隨 exponent 變化的推導
- 最大可表示奇數的計算

**考研相關：** IEEE 754 浮點數表示、特殊值判斷、精度分析是台大/交大偶考的選擇題。

---

### Discussion 4 — RISC-V Intro & Control Flow

**主題：** RISC-V 基本指令與控制流程  
**練習內容：**
- `lw`/`sw`/`slli`/`add`/`xori`/`addi` 指令行為追蹤（配合 array 記憶體佈局）
- C → RISC-V 翻譯：算術運算、pointer array 操作、if-else、for loop
- RISC-V → C 反向翻譯（看組語寫出等價 C）
- Linked list struct 在記憶體中的佈局（`val` + `next` pointer, tightly packed）
- Calling convention 基礎：`a0`-`a7` 傳參、`a0` 返回值、`sp` stack pointer
- 實作 `sumSquare` 函式（含 prologue/epilogue）

**考研相關：** RISC-V 指令語意、C↔Assembly 翻譯、calling convention 是考研核心考點。

---

### Discussion 5 — CALL (Compile → Assemble → Link → Load)

**主題：** 程式從 C 到執行的完整流程  
**練習內容：**
- Stored Program concept 的意義
- Assembler 兩趟掃描（two-pass）的原因
- Object file 六大組成：Header、Text、Data、Relocation Table、Symbol Table、Debug Info
- 辨認 pseudoinstruction（`la`、`li`、`mv`、`j`）及其展開
- Symbol table 與 Relocation table 內容推導
- RISC-V 定址模式：base displacement、PC-relative、register addressing
- Branch / Jump 指令的可達範圍計算
- 手動填寫 RISC-V 機器碼欄位（opcode、funct3、funct7、imm）

**考研相關：** 指令編碼格式、定址模式、branch 可達範圍是計組常考計算題。

---

### Discussion 6 — Boolean Logic, SDS (State), FSM

**主題：** 布林代數化簡、時序電路、有限狀態機  
**練習內容：**
- 九大布林代數定律應用：De Morgan's、Absorption、Distributive 等
- 化簡布林表達式（如 `(A+B)(A+B̄)C`）
- 邏輯閘辨認（AND、OR、NOT、NAND、XOR、XNOR）
- 用 NAND gates 建構 AND gate
- Register 時序分析：clk-to-q delay、setup time、hold time
- 填寫 timing diagram（含 NOT gate propagation delay）
- 計算最大允許 hold time 與最小 clock cycle time
- FSM 設計：辨認 bitstring pattern、偵測連續重複 bit、實作 regex `{10+1}`

**考研相關：** 布林代數化簡、timing analysis（critical path / setup / hold）、FSM 設計是數位邏輯常考題型。

---

### Discussion 7 — RISC-V Single Cycle Datapath

**主題：** 單週期 CPU datapath 與 control signal  
**練習內容：**
- 辨認 datapath 五大階段（IF / ID / EX / MEM / WB）的元件名稱
- 填寫 control signal 表格：`PCSel`、`ImmSel`、`BrUn`、`ASel`、`BSel`、`ALUSel`、`MemRW`、`RegWEn`、`WBSel`（對應 add、ori、lw、sw、beq、jal、bltu）
- 計算各指令使用的 datapath 階段與執行時間
- 辨認 critical path（最慢指令 = lw，經過全部五階段）
- 分析為何單週期 CPU 效率低（所有指令都要用最慢指令的 cycle time）

**考研相關：** Control signal 表格填寫、critical path 計算是台大/交大計組大題的經典考法。

---

### Discussion 8 — RISC-V Pipelining and Hazards

**主題：** Pipeline 時序分析與三種 hazard  
**練習內容：**
- Pipeline register 的用途、為何需要多次保存 instruction
- 效能分析：單週期 vs. 五級 pipeline 的 clock time 計算（含元件 delay 表）
- Structural hazard：RegFile double-pumping、IMEM/DMEM 分離
- Data hazard 偵測與 forwarding 路徑（EX→EX、MEM→EX）
- Load-use hazard：為何 forwarding 無法解決（lw 後緊接 dependent instruction 必須 stall 1 cycle）
- 指令重排（compiler scheduling）消除 stall
- Hazard detection 的 pseudo-code 邏輯：`rs1(n+1)==rd(n) || rs2(n+1)==rd(n) && RegWEn(n)==1`
- Control hazard：branch prediction、speculation、flush
- 完整 pipeline diagram 填寫（含 stall bubble）

**考研相關：** Pipeline hazard 分析（data/control）、forwarding 條件、stall 計算是考研計組**最高頻考點**（每年每校必考）。

---

### Discussion 9 — Caches

**主題：** Cache 結構、miss 分類、AMAT 計算  
**練習內容：**
- Tag / Index / Offset (T/I/O) bit 數計算
- Direct-mapped cache 的 hit/miss/replace 手動推導（逐次 access 追蹤 cache 狀態）
- 2-way set associative cache 的 hit/miss/replace 推導（含 LRU replacement）
- 3C miss 分類：Compulsory / Conflict / Capacity（用 fully-associative 假設法判斷）
- Code analysis：分析 C 程式（array stride access）的 cache hit rate
- Multi-level cache AMAT 公式：`Hit Time + Miss Rate × Miss Penalty`
- Global miss rate vs. Local miss rate 的區分
- 計算添加 L3 cache 後的 AMAT 與最大允許 hit time

**考研相關：** Cache T/I/O 計算、hit rate 分析、AMAT 多級 cache 計算是考研計組**最高頻考點**（與 pipeline 並列）。

---

### Discussion 10 — OS & Virtual Memory

**主題：** 作業系統基礎、虛擬記憶體、TLB  
**練習內容：**
- OS 職責：載入程式、資源多工、supervisor mode、system call
- `fork()` 行為：parent/child process 的返回值差異、變數複製
- Virtual Address → Physical Address 翻譯：VPN + Page Offset → PPN + Page Offset
- Page Table 結構：Valid bit、Dirty bit、Permission bits、PPN
- Page Fault 處理流程（disk → memory → page table → TLB 更新）
- Protection Fault（segmentation fault）的成因
- TLB：fully-associative cache for page table，LRU replacement
- 完整 TLB 狀態追蹤（6 次 memory access 後的 VPN/PPN/Valid/Dirty/LRU 更新）

**考研相關：** Virtual memory address translation、TLB hit/miss 判定、Page Fault 處理是考研計組/OS 高頻考點。

---

### Discussion 11 — I/O (Polling & Interrupts)

**主題：** I/O 控制方式  
**練習內容：**
- Polling vs. Interrupts 的定義、優缺點比較表
- Memory-Mapped I/O：用 `lw`/`sw` 讀寫特定 I/O address（Receiver/Transmitter Control & Data registers）
- 實作 RISC-V busy-wait I/O：讀取 Receiver ready bit → 讀 data → 等 Transmitter ready → 寫 data

**考研相關：** Polling vs. Interrupt 比較、Memory-Mapped I/O 概念是 CO/OS 偶考選擇題。

---

### Discussion 12 — Data-Level Parallelism (SIMD)

**主題：** Flynn's Taxonomy、SIMD intrinsics 程式設計  
**練習內容：**
- Flynn's Taxonomy 四類：SISD、SIMD、MISD、MIMD 的定義與範例
- Intel SSE intrinsics 操作：`_mm_set1_epi32`、`_mm_loadu_si128`、`_mm_mullo_epi32`、`_mm_add_epi32`、`_mm_storeu_si128`、`_mm_and_si128`、`_mm_cmpeq_epi32`
- 填空練習：向量自乘、array 元素 +1、array 前半加後半、條件 mask（不等於 5 則清零）
- 向量化 `product_naive`：處理 tail case（array 長度非 4 倍數）

**考研相關：** Flynn's Taxonomy 分類是選擇題常客；SIMD 程式設計本身較少直接出題，但概念會在效能分析題中出現。

---

### Discussion 13 — Cache Coherency, Atomics & Thread-Level Parallelism (OpenMP)

**主題：** 多核一致性、原子操作、OpenMP 平行程式設計  
**練習內容：**
- Cache incoherence 問題與 `volatile` 的作用
- RISC-V 原子指令：`lr.w`/`sc.w`（Load-Reserved / Store-Conditional）、`amoswap`
- Test-and-Set (TAS) 與 Compare-and-Swap (CAS) 的 RISC-V 實作
- 用 LR/SC 實作 ordered thread execution（依序執行 4 個 thread）
- OpenMP 程式分析：判斷 `#pragma omp parallel` vs. `#pragma omp parallel for` 的行為差異
- 識別 data race（Fibonacci 依賴、shared variable 競爭）
- 用 `#pragma omp critical` 和 `#pragma omp reduction` 修正 race condition
- Amdahl's Law 計算：給定可平行化比例與核心數，求 speedup

**考研相關：** Amdahl's Law 計算是台大/交大常考；lr/sc、TAS/CAS 概念偶考（交大 110 直接考 `ll`/`sc`）；OpenMP 概念在 OS 進階考題出現。

---

### Discussion 14 — MapReduce, Spark, WSC, RAID, ECC

**主題：** 分散式計算、資料中心、磁碟冗餘、錯誤校正碼  
**練習內容：**
- **Hamming ECC**：parity bit 位置（2 的冪次）、覆蓋範圍推導、SEC（Single Error Correction）編碼與解碼、SECDED（加一個 overall parity bit 偵測 double error）
- **RAID**：RAID 0–5 各級的優缺點比較表（striping / mirroring / dedicated parity / distributed parity）
- **MapReduce**：寫 pseudocode 的 `map()` / `reduce()`（coin counting → money calculation）
- **Spark**：用 RDD transform（`map`、`flatMap`、`reduceByKey`）+ action（`reduce`）實作同樣的 coin counting 與 GPA 計算
- **Warehouse-Scale Computing**：PUE（Power Usage Effectiveness）計算、估算 Google 年度電費、PUE 改善的成本節省

**考研相關：** Hamming Code 計算（parity bit 數量、錯誤位置偵測）是交大/台大偶考；RAID 級別比較是 OS 考試常考選擇題；MapReduce/Spark 較少直接出題。
