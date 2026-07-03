# 計組考研閱讀清單（白算盤 + 黑算盤 + 補充教材）

> **⚠️ 注意**：各校「計系」考卷多為 **OS + CO 合考**，本清單只涵蓋「計算機組織」部分。各校 CO 佔比與難度如下：
>
> | 學校 | CO 佔比（估） | CO 難度 |
> |------|-------------|--------|
> | 台大 | ~50% | 高（GPU/HPC/Roofline/big.LITTLE 等前沿主題） |
> | 交大 | ~40% | 中高（ISA encoding、Hamming code、pipeline 計算） |
> | 中正 | ~40% | 中（FF timing、pipeline basics、cache、IEEE 754） |
> | 師大 | ~30% | 基礎（CPI 計算、forwarding、AMAT、Amdahl） |
> | 中央 | ~25% | 中（dynamic scheduling、cache coherence） |
> | 成大 | ~20% | 中（DMA/I/O、cache） |

> **教材一覽**
>
> | 代號 | 書名 | 用途 |
> |------|------|------|
> | **RV** | Patterson & Hennessy, *Computer Organization and Design*, **RISC-V Edition, 2nd (2020)**（白算盤） | 主讀本，基礎 CO 全覆蓋 |
> | **M4** | Patterson & Hennessy, *Computer Organization and Design*, **MIPS Edition, 4th (2009)**（白算盤） | 補 ISA 差異與 I/O 深度 |
> | **QA6** | Hennessy & Patterson, *Computer Architecture: A Quantitative Approach*, **6th (2019)**（黑算盤） | 進階：OoO/Superscalar/GPU/DLP/TLP/WSC；台大出題水準對標此書 |
> | **Mano** | M. Morris Mano, *Digital Design*, **6th** | 補 FF timing / sequential circuit（Ch5 §5.4–5.5, Ch6 §6.2） |
> | **CUDA** | NVIDIA, *CUDA C++ Programming Guide*（免費線上） | CUDA memory model, warp/block/grid（Ch1–5） |
> | **H100 WP** | NVIDIA, *H100 Tensor Core GPU Architecture Whitepaper*（免費下載） | NVLink, HBM3, SM 架構規格 |
> | **GH200 WP** | NVIDIA, *Grace Hopper Superchip Architecture Whitepaper*（免費下載） | Grace Hopper 統一記憶體、NVLink-C2C；台大 114 直接引用 |
> | **大碩** | 大碩講義 | 僅列對照，非主軸 |
>
> **標記說明**
> - 🔶 **ISA-sensitive**：題目答案會因 MIPS / RISC-V 而不同，做題要先認題本用哪套
> - 🆕 **RV-only**：RISC-V 2nd 有、MIPS 4th 沒有（多為改版新增）
> - 📦 **M4-only / M4 較深**：MIPS 4th 有專章或講得比 RV 版完整
> - ✅ **ISA-free**：兩版一字不差，共用一套筆記即可
> - ⭐ **近年必考 / 高頻**
> - 🔷 **QA6 進階**：需要讀黑算盤才能完全掌握（主要針對台大、交大）

---

## A. 效能與基礎 Fundamentals & Performance

| 主題 | 說明 | RV 2nd | M4 | 大碩 |
|---|---|---|---|---|
| Introduction, technology, abstraction | 五層抽象（compiler→OS→ISA→microarch→gate）、Moore's Law、製程節點 | §1.1–1.5 | §1.1–1.3 | Ch1 重點1–3 |
| 🆕 Eight Great Ideas | parallelism、prediction、hierarchy 等八大設計原則，貫穿全書 | §1.2 | — | — |
| ⭐ Performance (CPU time = IC × CPI × Tc) | $\text{CPU time} = \text{IC} \times \text{CPI} \times T_c$；各因子由誰決定（compiler/ISA/microarch/technology） | §1.6 | §1.4 | Ch3 重點1–2 |
| ⭐ Power Wall | 動態功耗 $P = C \cdot V^2 \cdot f$；為何頻率停在 ~4 GHz、Dennard scaling 失效 | §1.7 | §1.5 | — |
| Uniprocessor → Multiprocessor 轉折 | 因 power wall 轉向多核；single-thread performance 成長趨緩的歷史脈絡 | §1.8 | §1.6 | — |
| ⭐ Amdahl's Law | $\text{Speedup} = 1/((1-f) + f/S)$；平行化瓶頸在 serial fraction，考題常算加速比上界 | §1.9 內 / 全書引用 | §1.8 內 | Ch3 重點4 |
| MIPS-as-metric fallacy | 為何不能用 MIPS（million instructions/sec）比效能——CPI 不同、ISA 不同會誤導 | §1.10 | §1.8 | Ch3 重點3 |
| Benchmark / SPEC | SPEC CPU、geometric mean、workload 代表性；考題常給 SPECratio 算 mean | §1.9 | §1.7 | Ch3 重點5–6 |

**讀法**：這塊 ✅ ISA-free，公式題主力（CPU performance equation、Amdahl、power = C·V²·f）。RV 版把 performance 併在 Ch1；大碩獨立成 Ch3，公式更集中，可交叉看。

---

## B. 指令集架構 Instructions / ISA 🔶

**整章都是 ISA-sensitive，這是兩本差異最大的地方。**

| 主題 | 說明 | RV 2nd | M4 |
|---|---|---|---|
| Operations / operands / register | `add`/`sub`/`lw`/`sw` 等基本指令；register file 32 個暫存器的 convention | §2.2–2.3 | §2.2–2.3 |
| Signed / unsigned, two's complement | 二補數表示法、sign extension、`slti`/`sltiu` 判斷差異 | §2.4 | §2.4 |
| ⭐ Instruction formats & encoding | R/I/S/B/U/J 六種 format（RV）vs R/I/J 三種（MIPS）；手算 machine code 必備 | §2.5 | §2.5 |
| Logical operations | `and`/`or`/`xor`/`sll`/`srl`/`sra`；mask 操作、bit extraction | §2.6 | §2.6 |
| Branch / decision | `beq`/`bne`/`blt`；branch offset 計算（PC-relative，byte addressing） | §2.7 | §2.7 |
| ⭐ Procedure call（caller/callee-saved, stack frame） | `jal`/`jalr`；`$sp` stack frame layout、preserved vs temporary registers、遞迴展開 | §2.8 | §2.8 |
| 🔶 Wide immediates & addressing | RV: `lui`+`addi` 組 32-bit；MIPS: `lui`+`ori`；addressing range 差異（PC-relative vs pseudodirect） | §2.10 | §2.10（32-bit imm） |
| Synchronization (ll/sc, atomics) | `lr.w`/`sc.w`（RV）或 `ll`/`sc`（MIPS）實作 test-and-set / CAS；用於 spinlock | §2.11 | §2.11 |
| Translate & start a program（compiler→assembler→linker→loader） | `.text`/`.data` section、symbol table、relocation、executable format、程式啟動流程 | §2.12 | §2.12 |

**兩版 ISA 關鍵差異（會滲進 Ch3/Ch4）：**
- 🔶 **Register 命名**：MIPS `$t0/$s0/$ra` ↔ RISC-V `x0–x31` (`t0/s0/ra/zero`)
- 🔶 **Instruction format**：MIPS 有 **J-type**（26-bit）；RISC-V **無 J-type**，改 U/UJ/SB 等，immediate 刻意打散（讓 sign bit 與 register field 位置固定，簡化硬體）
- 🔶 **Addressing modes**：MIPS 有 **pseudodirect**（J-type）；RISC-V `jal` 走 PC-relative 20-bit imm
- 🔶 **mult/div 介面**：MIPS 寫入 **HI/LO** register，用 `mfhi/mflo` 取出；RISC-V `mul/mulh/div/rem` 直接寫一般 register（→ 影響 Ch3 演算法的「介面」而非「硬體」）
- 🔶 **Real Stuff 對照對調**：M4 拿 ARM 當範例（§2.16）；RV 反過來拿 **MIPS 當 Real Stuff**（§2.16），再加 🆕 §2.18「Rest of the RISC-V ISA」

**讀法**：主讀 RV 2nd。做考古題時，遇到 machine code encoding / addressing range 題，先看題本 ISA，MIPS 題就翻 M4 §2.5 / §2.10 對照。

---

## C. 計算機算術 Computer Arithmetic

| 主題 | 說明 | RV 2nd | M4 | 大碩 |
|---|---|---|---|---|
| Addition / subtraction | ripple-carry adder、overflow detection（signed vs unsigned）、CLA 原理（大碩較深） | §3.2 | §3.2 | Ch2 重點2 |
| ✅ Multiplication（含 Booth's algorithm） | 迭代乘法器硬體（shift-add）、Booth's algorithm（signed 直接乘）、Wallace tree（大碩） | §3.3 | §3.3 | Ch2 重點7–8 |
| ✅ Division（restoring / non-restoring） | restoring（每步試減、不夠就加回）vs non-restoring（用 remainder sign 決定加/減） | §3.4 | §3.4 | Ch2 重點9–10 |
| ⭐✅ Floating Point（IEEE 754, add/mul flow, rounding, guard/round/sticky） | 1+8+23（single）/ 1+11+52（double）；normalize → align → add → normalize → round；denorm/∞/NaN 特殊值 | §3.5 | §3.5 | Ch2 重點11–14 |
| ✅ FP associativity 不成立 | $(a+b)+c \neq a+(b+c)$；因 rounding 順序不同結果不同，平行化須注意 | §3.5 內 | §3.6 | Ch2 重點15 |
| 🆕 Subword parallelism / SIMD | 一個 64-bit ALU 同時做 8 個 8-bit 加法（MMX/SSE 風格），向量化的硬體基礎 | §3.6 | —（此格是 associativity） | Ch2 重點3 |
| 🆕 Going Faster: subword + matrix multiply | DGEMM 用 subword SIMD 加速；貫穿全書的 matrix multiply 優化之一 | §3.8 | — | — |

**讀法**：乘除法硬體演算法 ✅ 完全 ISA-free（HI/LO 只是介面差，演算法一樣）。大碩把 CLA / carry-save adder（Ch2 重點5–6）拆得比原文書細，硬體加法器題可補大碩。**FP 是本章重心，必考**。🆕 subword parallelism 是 RV 版才有，M4 對應格被 FP associativity 佔掉——這是本章唯一版本差異。

---

## D. 處理器：單週期 Single-cycle Datapath & Control

| 主題 | 說明 | RV 2nd | M4 | QA6 / 補充 | 大碩 |
|---|---|---|---|---|---|
| Logic design conventions | combinational vs sequential 區分、clock methodology、edge-triggered 觀念 | §4.2 | §4.2 | — | 附錄 A（RV）/ 附錄 C（M4） |
| ⭐ Flip-flop timing（$T_{setup}$ / $T_{hold}$ / $T_{C2Q}$）、sequential circuit max freq | D-FF 三參數、critical path = $T_{C2Q}+T_{comb}+T_{setup}$、$f_{max}$ 計算、hold violation 與 buffer insertion | §4.2 / Appendix A | §4.2 / 附錄 C | **Mano Ch5 §5.4–5.5** | — |
| ⭐ Building a datapath | register file、ALU、sign-extend、PC+4 adder、branch adder 怎麼接；每條指令走哪條路 | §4.3 | §4.3 | — | Ch4 重點2 |
| ⭐ Simple (single-cycle) implementation + control | main control 7-bit truth table（`RegWrite`/`MemRead`/`ALUSrc`/...）、ALU control 二層解碼 | §4.4 | §4.4 | — | Ch4 重點2–3 |

**讀法**：datapath 畫圖 + control signal truth table 是主力題型。🔶 datapath 內的 **immediate generation** 因 RV immediate 打散而與 MIPS 長相不同，但控制邏輯的**觀念**共用。單週期效能瓶頸（Tc 被最慢指令綁死）在 §4.4 收尾。

**⚠️ Flip-flop timing**：中正、交大常考 FF timing constraint 與 critical path delay 計算（最大操作頻率 = $1/(T_{C2Q}+T_{cp}+T_{setup})$、hold time violation 修正）。原文書 §4.2 (RV) 或 Appendix A/C 有涵蓋，但需額外做過習題。交大也考過 ALU 組合邏輯 propagation delay 計算。**Mano Ch5 §5.4–5.5** 對 FF timing 講得更完整（setup/hold/propagation delay 的定義、時序圖範例），**Ch6 §6.2** 補 shift register 與 hold time fix（buffer insertion）——中正考過。只需讀這 ~60 頁，不需整本。

---

## E. 處理器：多週期 Multicycle（大碩附錄 / 原文書已淡化）

| 主題 | 說明 | RV 2nd | M4 | 大碩 |
|---|---|---|---|---|
| Multicycle datapath / FSM control / microprogramming | 每指令拆 3–5 cycles 共用 ALU；FSM 產生 control（state diagram）、microprogramming（microcode ROM）取代 hardwired | 附錄 C（Mapping Control to HW） | 附錄 D | 附錄「多重時脈」重點1–5 |

**讀法**：兩本白算盤正文都**不教 multicycle**，只在附錄提 control-to-hardware mapping（hardwired vs microprogrammed、FSM、sequencer）。NYCU/NTU 近年偏 pipeline，multicycle/microprogramming 出現率低——**看考古題分布再決定是否投入**，大碩附錄講得比原文書完整，真要考再翻大碩。

---

## F. 管線與危障 Pipelining & Hazards ⭐

**全書最重章節之一，畫圖題 + hazard 計算題主力。**

| 主題 | 說明 | RV 2nd | M4 | QA6 / 補充 | 大碩 |
|---|---|---|---|---|---|
| ⭐ Pipelining overview（IF/ID/EX/MEM/WB） | 五級切法、pipeline register 內容、throughput vs latency、理想 CPI=1 | §4.5 | §4.5 | QA6 Appendix C.1 | Ch5 重點1 |
| ⭐ Pipelined datapath + control | 每級 control 訊號隨 pipeline register 傳遞；畫完整 pipelined datapath 是必考題型 | §4.6 | §4.6 | — | Ch5 重點2–3 |
| ⭐ Data hazards: forwarding / stalling / load-use | EX/MEM → EX forwarding、MEM/WB → EX forwarding 的 mux 條件；`lw` 後接 dependent → 必 stall 1 cycle | §4.7 | §4.7 | QA6 Appendix C.2 | Ch5 重點4–7 |
| ⭐🔶 Control hazards | branch 結果在 ID（RV）或 MEM（MIPS 某些實作）才知道 → flush/stall；MIPS delay slot vs RV predict-not-taken | §4.8 | §4.8 | — | Ch5 重點8 |
| ⭐ Branch prediction（BHT 1-bit / 2-bit / correlating） | 1-bit: loop 首尾各 miss 一次；2-bit: 容忍一次例外→loop 只尾巴 miss；考題算 accuracy | §4.8 內 | §4.8 內 | **QA6 Ch3 §3.3–3.4**（tournament, gshare） | Ch5 重點8 |
| Exceptions in pipeline | 多指令同時 exception 時取最早的；flush 後續指令、save EPC、跳 handler | §4.9 | §4.9 | — | Ch5 重點10 |
| 🔷 ILP: superscalar, dynamic scheduling, OoO | 多 issue（CPI<1）；Tomasulo 用 reservation station + CDB 解 WAR/WAW；ROB 維持 in-order commit | §4.10 | §4.10 | **QA6 Ch3 §3.4–3.9**（Tomasulo, ROB, speculation） | Ch5 重點9 |
| 🔷 Super-pipelining / VLIW | 深管線（>5 stages）提高 $f$ 但增加 hazard penalty；VLIW 靠 compiler 排 bundle、hardware 不做 hazard detection | — | — | **QA6 Ch3 §3.2（VLIW）, Appendix H** | — |
| Real Stuff pipeline | 實際處理器 pipeline 長度、分支預測正確率、cache miss penalty 等工程數據 | §4.11（🆕 ARM Cortex-A53 + i7） | §4.11（Opteron X4） | QA6 §3.12（i7 detailed pipeline） | — |
| 🆕 Going Faster: ILP + matrix multiply | DGEMM 用 loop unrolling + register renaming 壓低 CPI | §4.12 | — | — | — |

**🔶 唯一 ISA 差異但很關鍵——Control hazard：**
- **MIPS 有 1 個 branch delay slot** → M4 §4.8 會教 compiler 如何填 delay slot
- **RISC-V 無 delayed branch** → 走 branch prediction + flush
- 做 control hazard 題，MIPS 題本要考慮 delay slot、RISC-V 不用，**答案不同**

**讀法**：主讀 RV §4.5–4.9。forwarding unit / hazard detection unit 邏輯 ✅ 除 delay slot 外共用。🆕 ARM Cortex-A53 是 RV 版新增的 in-order pipeline 範例，有教學價值可讀。

**🔷 黑算盤進階（台大、交大適用）**：
- **Branch prediction 進階**：白算盤只講 1-bit / 2-bit BHT。**QA6 Ch3 §3.3–3.4** 深入 tournament predictor、correlating predictor (m,n)、gshare——台大 109 考過 branch prediction accuracy 計算。中正 111 直接考 1-bit vs 2-bit BHT 比較（loop 中的 misprediction 次數差異），需理解狀態機轉移。
- **動態排程（Tomasulo / ROB / Speculation）**：白算盤 §4.10 只簡介。**QA6 Ch3 §3.4–3.9** 完整教 Tomasulo algorithm（reservation station、CDB）、Reorder Buffer、hardware speculation。僅台大、交大偶爾出，其餘校不考。
- **VLIW**：白算盤不教。**QA6 Ch3 §3.2** 講 static multiple issue / VLIW vs superscalar——台大 108 提過 Itanium。
- **深管線對 hazard penalty 的影響**：中正 111 考過拆 ID 為 2 stages 後，load-use penalty 從 1 cycle 增為 2 cycles。

---

## G. 記憶體階層：快取 Cache ⭐

**CP 值最高的考點區，✅ 完全 ISA-free，兩版共用。**

| 主題 | 說明 | RV 2nd | M4 | QA6 / 補充 | 大碩 |
|---|---|---|---|---|---|
| ⭐ Locality（temporal / spatial） | temporal: 剛存取的會再存取；spatial: 鄰近也會被存取→決定 block size 與 prefetch 策略 | §5.1 | §5.1 | — | Ch6 重點1 |
| ✅ Memory technologies（SRAM/DRAM/Flash 集中講） | 6T SRAM（快、貴、cache 用）vs 1T1C DRAM（慢、密、main memory 用）vs Flash（非揮發）；refresh、row buffer | §5.2 | 散在 I/O 章 | QA6 Appendix B（Memory Hierarchy Review） | — |
| ⭐ Basics of caches（direct-mapped） | address 拆成 tag/index/offset；hit 判斷、valid bit；block size 對 miss rate 的影響 | §5.3 | §5.2 | — | Ch6 重點2–4 |
| ⭐ Cache performance（AMAT = hit time + miss rate × miss penalty） | $\text{AMAT} = \text{hit time} + \text{miss rate} \times \text{miss penalty}$；多層 cache 用 local vs global miss rate | §5.4 | §5.3 | — | Ch6 重點5 |
| ⭐ Set-associative / replacement (LRU) / write policy | n-way 降低 conflict miss；LRU 替換（考題追蹤 LRU stack）；write-through vs write-back、write-allocate vs no-write-allocate | §5.3–5.4 | §5.2–5.3 | — | Ch6 重點6 |
| Multilevel cache | L1（小、快、split I/D）→ L2（unified、降低 miss penalty）→ L3；inclusion vs exclusion policy | §5.4 內 | §5.3 內 | — | Ch6 重點7 |
| ⭐ 3C miss model（compulsory/capacity/conflict） | 冷啟動 miss、容量不足 miss、associativity 不足 miss；增加 block size/cache size/associativity 各消除哪類 | §5.8 | §5.5 | — | Ch6 重點13 |
| FSM cache controller | cache hit/miss 的狀態機：idle → compare tag → write-back（if dirty）→ allocate → done | §5.9 | §5.7 | — | Ch6 重點14 |
| Cache bandwidth: non-blocking (lockup-free), multi-banking, prefetch | non-blocking: miss 時不卡住後續 hit（MSHR 管理多筆 outstanding miss）；banking: 多 bank 平行存取提升頻寬 | §5.4 內 | §5.3 內 | **QA6 Ch2 §2.3**（10 advanced optimizations） | — |
| 🔷 Advanced cache optimizations（way prediction, victim cache, HW prefetch, compiler opt） | way prediction 省比較功耗；victim cache 抓被踢出的 block 降 conflict miss；stream buffer prefetch | — | — | **QA6 Ch2 §2.3** | — |
| Cache coherence（snooping, MESI） | 多核共享記憶體→每核 cache 可能不一致；snooping 靠 bus 廣播 invalidate/update；MESI 四態（Modified/Exclusive/Shared/Invalid） | §5.10 | §5.8 | **QA6 Ch5 §5.2–5.4**（directory-based, MOESI） | Ch8 重點5 |
| 🆕 Going Faster: cache blocking / loop tiling | 矩陣乘法分 tile 做，讓 working set 塞進 cache→降低 capacity miss | §5.15 | — | — | — |

**讀法**：write-through vs write-back、write-allocate、AMAT 計算、3C 分類都是高頻題。🆕 **cache blocking (loop tiling)** 是 RV 版才有的知識點，M4 找不到——若題庫有，只讀 RV §5.15。SRAM vs DRAM 特性比較（6T vs 1T1C：速度/密度/功耗/成本）中正曾直接出題。non-blocking cache 與 multi-banked cache 的頻寬優化也在中正 110 考過。

**🔷 黑算盤進階（台大、交大適用）**：**QA6 Ch2** 把 cache 優化擴展為 10 大類（way prediction、pipelined access、multibanked、non-blocking、critical word first、prefetch、compiler optimization、victim cache 等）。白算盤只提到 non-blocking 和 banking，QA6 更系統化。台大考 cache 時偶爾超出白算盤範圍（如 victim cache、HW prefetch policy）。cache coherence 方面，QA6 Ch5 §5.2–5.4 深入 directory-based protocol 和 memory consistency model——白算盤只教 snooping + MESI，台大/中央考過 directory-based。

---

## H. 記憶體階層：虛擬記憶體 Virtual Memory ⭐

**✅ ISA-free，高頻。注意兩版節次順序不同。**

| 主題 | 說明 | RV 2nd | M4 | 大碩 |
|---|---|---|---|---|
| ⭐ Virtual memory, page table, page fault | VA→PA 透過 page table（多層）；page fault 觸發 OS 從 disk swap in；dirty bit / reference bit | §5.7 | §5.4 | Ch6 重點8 |
| ⭐ TLB（address translation 加速） | fully-associative 小 cache 存最近的 PTE；TLB miss → page table walk；考題算 effective access time | §5.7 內 | §5.4 內 | Ch6 重點9 |
| ⭐ VIPT / PIPT（cache × VM 交互） | PIPT 無 aliasing 但慢（等 TLB）；VIPT 平行查 TLB+cache（index 用 VA、tag 用 PA）→L1 常用 | §5.7 內 | §5.4 內 | Ch6 重點10 |
| Protection mechanism | page table entry 的 R/W/X 權限 bit、user/kernel mode、base+bound → segmentation → paging 演進 | §5.7 內 | §5.4 內 | Ch6 重點11 |
| Common framework for memory hierarchy | 用 4 個問題統一 cache/VM/TLB：block placement、identification、replacement、write strategy | §5.8 | §5.5 | Ch6 重點12 |
| Virtual machines | hypervisor（VMM）攔截 privileged instruction；guest OS 跑在 user mode；hardware support（VT-x） | §5.6 | §5.6 | Ch6 重點15 |

**⚠️ 節次陷阱**：M4 是 VM(§5.4) → Common Framework(§5.5) → Virtual Machines(§5.6)；**RV 把 Virtual Machines (§5.6) 排在 Virtual Memory (§5.7) 之前**，Common Framework 移到 §5.8。你按 subchapter 標考古題時這裡最容易對錯。

---

## I. 可靠度、ECC、RAID Dependability

| 主題 | 說明 | RV 2nd | M4 | 大碩 |
|---|---|---|---|---|
| 🆕 Dependable memory hierarchy（放進 Ch5） | RV 版把 dependability 與 memory 整合在同一章，強調 memory 是故障熱點 | §5.5 | — | — |
| ⭐ ECC / Hamming code (SEC/SECDED) | parity 只能偵錯；Hamming SEC 需 $\lceil\log_2(m+r+1)\rceil$ 個 check bits；SECDED 再加 1 bit 做 double-error detect | §5.5 | §6.2 內 | — |
| Dependability, Reliability, Availability（MTTF/MTBF/MTTR） | $\text{Availability} = \text{MTTF}/(\text{MTTF}+\text{MTTR})$；disk array 的 MTTF 怎麼算（N 顆 disk 取倒數） | §5.5 | 📦 §6.2 | Ch7 重點3 |
| ⭐ RAID (0/1/5/6) | RAID 0 striping（無冗餘）、1 mirroring、5 distributed parity（容 1 顆壞）、6 dual parity（容 2 顆） | §5.11 | 📦 §6.9 | Ch7 重點4 |

**⚠️ 位置陷阱**：**ECC/Hamming 與 dependability 在 RV 版是 Ch5（記憶體章），在 M4 是 Ch6（I/O 章）。** 找同一知識點兩版跳不同章。availability 公式、Hamming SECDED bit 數計算是常見題型。

---

## J. 儲存與 I/O Storage & I/O 📦

**M4 有完整專章，RV 版拆散且縮水——這塊反而以 M4 為主。**

| 主題 | 說明 | RV 2nd | M4 | 大碩 |
|---|---|---|---|---|
| Disk / Flash storage | HDD：seek time + rotational latency + transfer time；SSD：page/block、wear leveling、FTL | §5.2 內（縮） | 📦 §6.3–6.4 | Ch7 重點2 |
| Bus（synchronous/asynchronous, arbitration, bandwidth） | synchronous 靠 clock、asynchronous 靠 handshaking；arbitration（daisy chain / centralized / distributed）；bandwidth 計算 | — | 📦 §6.5 | Ch7 重點5–8 |
| ⭐ I/O 溝通：polling / interrupt / DMA | polling 忙等 CPU；interrupt 讓 CPU 做別的事；DMA 讓 I/O controller 直接搬 memory（考題算 CPU 使用率） | — | 📦 §6.6 | Ch7 重點9–12 |
| I/O system performance & design | I/O bottleneck 分析、disk throughput vs CPU bandwidth 匹配、RAID + cache 整合設計 | — | 📦 §6.7–6.8 | Ch7 重點13 |

**讀法**：📦 **DMA、bus arbitration、I/O system design 這些 RV 2nd 幾乎砍光**，只能看 M4 Ch6。台灣考研 **DMA / RAID 會出**，大碩 Ch7 補得比 M4 還滿——這塊建議**大碩 Ch7 + M4 Ch6 為主，RV 跳過**。

---

## K. 多處理器與平行 Multiprocessors & Parallelism ⭐

| 主題 | 說明 | RV 2nd | M4 | QA6 / 補充 | 大碩 |
|---|---|---|---|---|---|
| ⭐ Flynn taxonomy (SISD/SIMD/MIMD/SPMD) | SISD（單核）、SIMD（向量/GPU）、MIMD（多核/cluster）、SPMD（一份程式跑多 thread，GPU 常見模式） | §6.3 | §7.6 | — | Ch8 重點7 |
| ⭐ Hardware multithreading（fine/coarse-grained, SMT） | fine-grained: 每 cycle 切 thread 藏 latency；coarse-grained: cache miss 才切；SMT: 同 cycle 多 thread 共用 FU（如 Intel HT） | §6.4 | §7.5 | **QA6 Ch3 §3.12**（SMT in i7） | Ch8 重點6 |
| Multicore / shared-memory multiprocessor | 多核共享 L2/L3 + main memory；UMA vs NUMA；需 coherence + synchronization（lock/barrier） | §6.5 | §7.3 | **QA6 Ch5 §5.1–5.3** | Ch8 重點3 |
| 🔷 Memory consistency models（SC, TSO, relaxed） | SC: 所有核看到同一全域順序；TSO: store 可延遲但 load 不繞過 store（x86 用）；relaxed: 需 fence 指令 | — | — | **QA6 Ch5 §5.6** | — |
| Message-passing / MPP / clusters / WSC | 不共享記憶體，靠 send/recv 通訊（MPI）；WSC = 大規模 cluster（Google 等級），強調 tail latency、PUE | §6.7（🆕 WSC 擴充） | §7.4 | **QA6 Ch6**（WSC 完整章） | Ch8 重點4 |
| Cache coherence（跨接 §G） | snooping（bus broadcast，不 scalable）vs directory（集中記錄 sharer list，scalable）；見 §G 的 MESI 說明 | §5.10 | §5.8 | **QA6 Ch5 §5.2–5.4**（directory-based） | Ch8 重點5 |

**讀法**：✅ ISA-free。Flynn 分類、multithreading 三型是定義題主力。🆕 warehouse-scale computing / cloud 在 RV 版擴充。

**🔷 黑算盤進階（台大適用）**：**QA6 Ch5** 整章講 Thread-Level Parallelism，包含 directory-based coherence（白算盤只教 snooping）和 memory consistency model（sequential consistency、TSO）——台大偶爾考。**QA6 Ch6** 整章講 Warehouse-Scale Computing（Google WSC、PUE、tail latency）——台大前沿題可能觸及。

---

## L. GPU 🆕⭐🔷（近年必考——重點看這區）

> **⚠️ 主要出現於台大。** 台大 114 年 GPU/NVIDIA GH200/MLPerf 題目佔該年 50%+。交大/中正/師大幾乎不出 GPU 題。若目標校非台大，本節可降為選讀。

| 主題 | 說明 | RV 2nd | M4 | QA6 / NVIDIA 文件 |
|---|---|---|---|---|
| ⭐ Intro to GPU（正文） | 為何 GPU 比 CPU 快：大量簡單核 × SIMT、throughput-oriented 設計哲學 | §6.6 | §7.7 | — |
| GPU system architectures | GPU 與 CPU 透過 PCIe 連接、discrete vs integrated、host↔device 資料搬移成本 | 附錄 B.2 | 附錄 A.2 | — |
| ⭐ Programming GPUs（CUDA model） | grid → block → thread 三層結構；`__global__` kernel launch；`threadIdx`/`blockIdx` 定址；shared memory 做 tile | 附錄 B.3 | 附錄 A.3 | **CUDA Guide Ch1–5** |
| ⭐ Multithreaded multiprocessor architecture（SM, warp） | SM 內 32-thread warp 同步執行（SIMT）；warp scheduler 發射指令；warp divergence 造成效能損失 | 附錄 B.4 | 附錄 A.4 | **QA6 Ch4 §4.4**（GPU arch 深入） |
| Parallel memory system | GPU memory hierarchy: register → shared mem（scratchpad）→ L1/L2 → global（HBM）；coalesced access 很重要 | 附錄 B.5 | 附錄 A.5 | **CUDA Guide Ch5**（memory hierarchy） |
| GPU floating point arithmetic | GPU 的 FP32/FP64 throughput 比（通常 2:1 或 32:1）；Tensor Core 的 mixed-precision（FP16→FP32 accumulate） | 附錄 B.6 | 附錄 A.6 | — |
| Real Stuff: NVIDIA GeForce 8800 | 白算盤的 GPU 範例（2006 年），觀念仍通用但規格數字已過時 | 附錄 B.7 | 附錄 A.7 | — |
| Mapping applications to GPUs | 如何把演算法對應到 GPU：資料平行拆分、occupancy 調校、memory 存取 pattern 優化 | 附錄 B.8 | 附錄 A.8 | — |
| 🔷 SIMD / Vector Processors（GPU 的前身觀念） | vector register + vector FU pipeline（Cray 風格）；AVX/SSE 是 x86 的 SIMD 擴充；GPU 可視為 SIMT ⊃ SIMD | — | — | **QA6 Ch4 §4.1–4.3**（vector arch, SIMD extensions） |
| 🔷 DNN accelerators（TPU, systolic array） | Google TPU v1: 8-bit int MAC 的 systolic array（256×256），專做 inference；v2/v3 加 HBM 做 training | — | — | **QA6 Ch7 §7.3–7.4**（Google TPU, DNN hardware） |
| 🔷 NVIDIA H100 / Hopper architecture | 132 SM、128 CUDA cores + 4 Tensor Cores/SM、NVLink 4.0（900 GB/s）、80 GB HBM3（3.35 TB/s）、Thread Block Cluster | — | — | **H100 WP**（SM 架構, NVLink 4.0, HBM3, Tensor Core） |
| 🔷 NVIDIA GH200 Grace Hopper Superchip | Grace CPU（Arm Neoverse）+ Hopper GPU 單晶片；NVLink-C2C（900 GB/s）統一 CPU+GPU 記憶體、96/144 GB HBM3/3e | — | — | **GH200 WP**（統一記憶體, NVLink-C2C, 72GB HBM3） |
| 🔷 MLPerf / AI inference benchmarks | 業界標準 AI benchmark：分 training / inference / HPC；比較不同硬體的 throughput 與 latency | — | — | **QA6 Ch7 §7.7** + NVIDIA 官方 MLPerf 結果 |

**讀法（三層式）**：

1. **基礎層（白算盤）**：先讀 RV 附錄 B.3–B.4（SM hierarchy、warp scheduling、CUDA memory model、SIMT vs SIMD）。兩版 GPU 附錄內容幾乎相同（都以 GeForce 8800 為例），主讀 RV 版即可。
2. **進階層（黑算盤 QA6）**：
   - **QA6 Ch4 §4.1–4.3**：Vector Processors → SIMD extensions → GPU 的演進脈絡。§4.4 把 GPU 拆得比白算盤細（NVIDIA Tesla vs Intel i7 的對比分析）。
   - **QA6 Ch7 §7.3–7.4**：Domain-Specific Architectures——Google TPU v1/v2/v3 的 systolic array、DNN inference vs training 硬體差異。台大愛考「比較 GPU vs TPU vs CPU 的設計取捨」。
   - **QA6 Ch7 §7.7**：MLPerf benchmark 的設計理念與結果解讀。
3. **前沿層（NVIDIA Whitepaper）**：台大 114 直接引用 GH200 規格出題。需要掌握的數字：
   - **H100 WP**：132 個 SM、each SM 128 CUDA cores + 4 Tensor Cores（4th gen）、NVLink 4.0（900 GB/s）、80 GB HBM3（3.35 TB/s）
   - **GH200 WP**：Grace CPU + Hopper GPU unified memory（NVLink-C2C 900 GB/s）、96 GB HBM3 或 144 GB HBM3e
   - **CUDA Guide Ch1–5**：理解 thread hierarchy（grid → block → thread）、memory hierarchy（register → shared → global → unified）、warp divergence、occupancy
   
> **建議讀書順序**：白算盤 Appendix B.3–B.4 → QA6 Ch4 §4.4 → QA6 Ch7 → CUDA Guide Ch1–5 → H100/GH200 Whitepaper

---

## M. 互連網路與效能模型 Interconnect & Roofline

| 主題 | 說明 | RV 2nd | M4 | QA6 / 補充 | 大碩 |
|---|---|---|---|---|---|
| Network topologies（mesh, torus, hypercube） | mesh: $\sqrt{N} \times \sqrt{N}$ 2D grid；torus: mesh + wrap-around link；hypercube: $\log_2 N$ 維度每點連 $\log_2 N$ 鄰居 | §6.8 | §7.8 | **QA6 Appendix F**（interconnect 完整附錄） | Ch8 重點9 |
| 🔷 Bisection bandwidth / diameter / routing | bisection BW = 切半後跨越的 link 數 × link BW；diameter = 最遠兩點的 hop 數；deadlock-free routing | — | — | **QA6 Appendix F.2–F.4** | — |
| Cluster networking | InfiniBand / Ethernet、fat-tree topology（常見於 HPC cluster）、switch hierarchy | §6.9 | — | — | — |
| ⭐ Roofline model（主要考台大） | $\text{Perf} = \min(\text{peak FLOPS}, \text{BW} \times \text{OI})$；以 operational intensity 判斷 compute-bound vs memory-bound | §6.10–6.11 | §7.10–7.11 | **QA6 Ch4 §4.7**（Roofline for GPU） | — |
| 🆕 Going Faster: multiple processors + matrix multiply | 多核平行化 DGEMM；strong scaling vs weak scaling、通訊 overhead | §6.12 | — | — | — |

**讀法**：✅ 兩版都有 Roofline（M4 在 §7.10）。topology 的 diameter / bisection bandwidth 計算是常見題。Roofline（operational intensity vs performance bound）你 HPC 報告用過，觀念熟。

**🔷 黑算盤進階**：若台大考 interconnect topology 的深入計算（bisection bandwidth、diameter、路由演算法），**QA6 Appendix F** 有完整的 interconnection networks 附錄（~50 頁），白算盤只是淺帶。Roofline 方面，**QA6 Ch4 §4.7** 有專門針對 GPU 的 Roofline 分析（Tesla vs i7），可對照台大出題。

---

## N. 積體電路基礎 IC Basics

| 主題 | 說明 | RV 2nd | M4 | 大碩 |
|---|---|---|---|---|
| IC fabrication, wafer, die yield, cost | wafer → die 切割；$\text{yield} = (1 + \text{defects/area} \times \text{die area} / N)^{-N}$；cost per die = wafer cost / (dies per wafer × yield) | §1.5 內 | §1.7 內 | Ch9 重點1–3 |

**讀法**：很短，cost per die 與 yield 公式背起來。原文書散在 Ch1；大碩獨立成 Ch9，公式更集中，可看大碩。

---

## O. 只在 MIPS 4th、可略讀

| 主題 | 說明 | M4 |
|---|---|---|
| 📦 Assemblers, Linkers, SPIM（附錄 B） | pseudo-instruction 展開、symbol table 建立、relocation record、SPIM 模擬器操作；RV 版整個拿掉。若考 linker/loader 細節才需翻 | 附錄 B |

---

## 考古題出題頻率 Top 5

1. **Pipeline hazards & forwarding**（全校必考）
2. **Cache（AMAT / 3C / set-associative）**（全校必考）
3. **CPU performance equation & Amdahl's Law**（全校必考）
4. **IEEE 754 浮點數**（全校必考）
5. **ISA encoding（MIPS 為主）**（交大、中正常考）

> 以上五類佔全部 CO 題超過 70%。

---

## 讀書順序建議（時間軸）

### Phase 1：白算盤基礎（所有學校必備）

1. **地基**：A 效能 → B ISA（主讀 RV，建立 register/format 兩套對照）
2. **算術**：C（重壓 FP）
3. **數位邏輯補充**：Mano Ch5 §5.4–5.5（FF timing）→ Ch6 §6.2（shift register）——搭配 §D 一起讀
4. **處理器**：D 單週期 → F 管線（重壓 hazard；記 delay slot 版本差）→（E 多週期看考古題決定）
5. **記憶體**：G 快取 → H 虛擬記憶體 → I ECC/RAID（記位置陷阱：RV 在 Ch5、M4 在 Ch6）
6. **I/O**：J（以大碩 Ch7 + M4 Ch6 為主）
7. **平行**：K 多處理器 → L GPU（白算盤附錄 B.3–B.4）→ M Roofline/topology
8. **收尾**：N IC → O 補漏

### Phase 2：黑算盤進階（台大、交大必備）

> 以下按優先順序排列，時間不夠的話讀到哪算到哪。

1. **QA6 Ch3**（ILP）：§3.3–3.4 branch prediction 進階 → §3.4–3.9 Tomasulo / ROB / speculation → §3.2 VLIW
2. **QA6 Ch4**（DLP）：§4.1–4.3 vector / SIMD → **§4.4 GPU architecture**（核心！）→ §4.7 Roofline for GPU
3. **QA6 Ch5**（TLP）：§5.2–5.4 directory-based coherence → §5.6 memory consistency
4. **QA6 Ch7**（DSA）：§7.3–7.4 TPU / DNN hardware → §7.7 MLPerf
5. **QA6 Ch2**（Memory）：§2.3 十大 cache 優化（選讀，台大偶考 victim cache / HW prefetch）
6. **QA6 Ch6**（WSC）：選讀，台大前沿題可能觸及
7. **QA6 Appendix F**（Interconnect）：選讀，topology 深入計算

### Phase 3：NVIDIA 前沿（台大 114 級以後適用）

1. **CUDA C++ Programming Guide Ch1–5**：thread/memory hierarchy、warp divergence、occupancy
2. **H100 Whitepaper**：SM 架構、NVLink 4.0、HBM3 規格
3. **GH200 Whitepaper**：Grace Hopper 統一記憶體、NVLink-C2C——台大 114 直接引用

---

## 黑算盤（QA6）章節速查表

| QA6 章節 | 主題 | 對應白算盤 | 本清單分區 |
|---------|------|----------|----------|
| Ch1 | Fundamentals, ISA（RISC-V） | RV Ch1–2 | §A, §B |
| **Ch2** | Memory Hierarchy Design（10 cache optimizations） | RV Ch5（基礎版） | §G |
| **Ch3** | ILP（Tomasulo, ROB, branch prediction, VLIW） | RV §4.8–4.10（簡介版） | §F |
| **Ch4** | DLP（Vector, SIMD, **GPU architecture**） | RV 附錄 B（GeForce 8800） | §L |
| **Ch5** | TLP（Coherence, Consistency, Directory） | RV §5.10 + §6.3–6.5 | §K, §G |
| **Ch6** | WSC（Warehouse-Scale Computing） | RV §6.7（縮水版） | §K |
| **Ch7** | DSA（**TPU**, DNN, MLPerf） | — | §L |
| Appendix C | Pipelining（detailed） | RV Ch4 | §F |
| Appendix F | Interconnection Networks | RV §6.8（簡介） | §M |

---

## 三個最容易對錯的坑（標考古題時注意）

- 🔶 **認 ISA 的題型**：只有 B 全部、F 的 control hazard（delay slot）、C 的 mult/div 介面。其餘全共用。
- ⚠️ **ECC / dependability / RAID 的章號**：RV 在 Ch5，M4 在 Ch6。
- ⚠️ **Ch5 內部順序**：RV 是 Virtual Machines(§5.6) 早於 Virtual Memory(§5.7)。

## RV-only 知識點清單（M4 找不到，別浪費時間翻）

Eight Great Ideas（§1.2）、subword parallelism（§3.6）、cache blocking / loop tiling（§5.15）、貫穿四章的 Going Faster matrix multiply（§3.8→4.12→5.15→6.12）、ARM Cortex-A53 in-order pipeline 範例（§4.11）、WSC 擴充（§6.7）。
