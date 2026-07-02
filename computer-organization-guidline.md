# 計組考研閱讀清單（以白算盤原文書為主）

> **主軸**：Patterson & Hennessy
> - **RV** = *Computer Organization and Design*, **RISC-V Edition, 2nd (2020)** — 主讀本，內容同第 6 版線
> - **M4** = *Computer Organization and Design*, **MIPS Edition, 4th (2009)** — 補 ISA 差異與 I/O 深度
> - **大碩** = 大碩講義（僅列對照，非主軸）
>
> **標記說明**
> - 🔶 **ISA-sensitive**：題目答案會因 MIPS / RISC-V 而不同，做題要先認題本用哪套
> - 🆕 **RV-only**：RISC-V 2nd 有、MIPS 4th 沒有（多為改版新增）
> - 📦 **M4-only / M4 較深**：MIPS 4th 有專章或講得比 RV 版完整
> - ✅ **ISA-free**：兩版一字不差，共用一套筆記即可
> - ⭐ **近年必考 / 高頻**

---

## A. 效能與基礎 Fundamentals & Performance

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| Introduction, technology, abstraction | §1.1–1.5 | §1.1–1.3 | Ch1 重點1–3 |
| 🆕 Eight Great Ideas | §1.2 | — | — |
| ⭐ Performance (CPU time = IC × CPI × Tc) | §1.6 | §1.4 | Ch3 重點1–2 |
| ⭐ Power Wall | §1.7 | §1.5 | — |
| Uniprocessor → Multiprocessor 轉折 | §1.8 | §1.6 | — |
| ⭐ Amdahl's Law | §1.9 內 / 全書引用 | §1.8 內 | Ch3 重點4 |
| MIPS-as-metric fallacy | §1.10 | §1.8 | Ch3 重點3 |
| Benchmark / SPEC | §1.9 | §1.7 | Ch3 重點5–6 |

**讀法**：這塊 ✅ ISA-free，公式題主力（CPU performance equation、Amdahl、power = C·V²·f）。RV 版把 performance 併在 Ch1；大碩獨立成 Ch3，公式更集中，可交叉看。

---

## B. 指令集架構 Instructions / ISA 🔶

**整章都是 ISA-sensitive，這是兩本差異最大的地方。**

| 主題 | RV 2nd | M4 |
|---|---|---|
| Operations / operands / register | §2.2–2.3 | §2.2–2.3 |
| Signed / unsigned, two's complement | §2.4 | §2.4 |
| ⭐ Instruction formats & encoding | §2.5 | §2.5 |
| Logical operations | §2.6 | §2.6 |
| Branch / decision | §2.7 | §2.7 |
| ⭐ Procedure call（caller/callee-saved, stack frame） | §2.8 | §2.8 |
| 🔶 Wide immediates & addressing | §2.10 | §2.10（32-bit imm） |
| Synchronization (ll/sc, atomics) | §2.11 | §2.11 |
| Translate & start a program（compiler→assembler→linker→loader） | §2.12 | §2.12 |

**兩版 ISA 關鍵差異（會滲進 Ch3/Ch4）：**
- 🔶 **Register 命名**：MIPS `$t0/$s0/$ra` ↔ RISC-V `x0–x31` (`t0/s0/ra/zero`)
- 🔶 **Instruction format**：MIPS 有 **J-type**（26-bit）；RISC-V **無 J-type**，改 U/UJ/SB 等，immediate 刻意打散（讓 sign bit 與 register field 位置固定，簡化硬體）
- 🔶 **Addressing modes**：MIPS 有 **pseudodirect**（J-type）；RISC-V `jal` 走 PC-relative 20-bit imm
- 🔶 **mult/div 介面**：MIPS 寫入 **HI/LO** register，用 `mfhi/mflo` 取出；RISC-V `mul/mulh/div/rem` 直接寫一般 register（→ 影響 Ch3 演算法的「介面」而非「硬體」）
- 🔶 **Real Stuff 對照對調**：M4 拿 ARM 當範例（§2.16）；RV 反過來拿 **MIPS 當 Real Stuff**（§2.16），再加 🆕 §2.18「Rest of the RISC-V ISA」

**讀法**：主讀 RV 2nd。做考古題時，遇到 machine code encoding / addressing range 題，先看題本 ISA，MIPS 題就翻 M4 §2.5 / §2.10 對照。

---

## C. 計算機算術 Computer Arithmetic

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| Addition / subtraction | §3.2 | §3.2 | Ch2 重點2 |
| ✅ Multiplication（含 Booth's algorithm） | §3.3 | §3.3 | Ch2 重點7–8 |
| ✅ Division（restoring / non-restoring） | §3.4 | §3.4 | Ch2 重點9–10 |
| ⭐✅ Floating Point（IEEE 754, add/mul flow, rounding, guard/round/sticky） | §3.5 | §3.5 | Ch2 重點11–14 |
| ✅ FP associativity 不成立 | §3.5 內 | §3.6 | Ch2 重點15 |
| 🆕 Subword parallelism / SIMD | §3.6 | —（此格是 associativity） | Ch2 重點3 |
| 🆕 Going Faster: subword + matrix multiply | §3.8 | — | — |

**讀法**：乘除法硬體演算法 ✅ 完全 ISA-free（HI/LO 只是介面差，演算法一樣）。大碩把 CLA / carry-save adder（Ch2 重點5–6）拆得比原文書細，硬體加法器題可補大碩。**FP 是本章重心，必考**。🆕 subword parallelism 是 RV 版才有，M4 對應格被 FP associativity 佔掉——這是本章唯一版本差異。

---

## D. 處理器：單週期 Single-cycle Datapath & Control

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| Logic design conventions | §4.2 | §4.2 | 附錄 A（RV）/ 附錄 C（M4） |
| ⭐ Building a datapath | §4.3 | §4.3 | Ch4 重點2 |
| ⭐ Simple (single-cycle) implementation + control | §4.4 | §4.4 | Ch4 重點2–3 |

**讀法**：datapath 畫圖 + control signal truth table 是主力題型。🔶 datapath 內的 **immediate generation** 因 RV immediate 打散而與 MIPS 長相不同，但控制邏輯的**觀念**共用。單週期效能瓶頸（Tc 被最慢指令綁死）在 §4.4 收尾。

---

## E. 處理器：多週期 Multicycle（大碩附錄 / 原文書已淡化）

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| Multicycle datapath / FSM control / microprogramming | 附錄 C（Mapping Control to HW） | 附錄 D | 附錄「多重時脈」重點1–5 |

**讀法**：兩本白算盤正文都**不教 multicycle**，只在附錄提 control-to-hardware mapping（hardwired vs microprogrammed、FSM、sequencer）。NYCU/NTU 近年偏 pipeline，multicycle/microprogramming 出現率低——**看考古題分布再決定是否投入**，大碩附錄講得比原文書完整，真要考再翻大碩。

---

## F. 管線與危障 Pipelining & Hazards ⭐

**全書最重章節之一，畫圖題 + hazard 計算題主力。**

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| ⭐ Pipelining overview（IF/ID/EX/MEM/WB） | §4.5 | §4.5 | Ch5 重點1 |
| ⭐ Pipelined datapath + control | §4.6 | §4.6 | Ch5 重點2–3 |
| ⭐ Data hazards: forwarding / stalling / load-use | §4.7 | §4.7 | Ch5 重點4–7 |
| ⭐🔶 Control hazards | §4.8 | §4.8 | Ch5 重點8 |
| Exceptions in pipeline | §4.9 | §4.9 | Ch5 重點10 |
| ILP: superscalar, dynamic scheduling, OoO | §4.10 | §4.10 | Ch5 重點9 |
| Real Stuff pipeline | §4.11（🆕 ARM Cortex-A53 + i7） | §4.11（Opteron X4） | — |
| 🆕 Going Faster: ILP + matrix multiply | §4.12 | — | — |

**🔶 唯一 ISA 差異但很關鍵——Control hazard：**
- **MIPS 有 1 個 branch delay slot** → M4 §4.8 會教 compiler 如何填 delay slot
- **RISC-V 無 delayed branch** → 走 branch prediction + flush
- 做 control hazard 題，MIPS 題本要考慮 delay slot、RISC-V 不用，**答案不同**

**讀法**：主讀 RV §4.5–4.9。forwarding unit / hazard detection unit 邏輯 ✅ 除 delay slot 外共用。🆕 ARM Cortex-A53 是 RV 版新增的 in-order pipeline 範例，有教學價值可讀。

---

## G. 記憶體階層：快取 Cache ⭐

**CP 值最高的考點區，✅ 完全 ISA-free，兩版共用。**

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| ⭐ Locality（temporal / spatial） | §5.1 | §5.1 | Ch6 重點1 |
| 🆕 Memory technologies（SRAM/DRAM/Flash 集中講） | §5.2 | 散在 I/O 章 | — |
| ⭐ Basics of caches（direct-mapped） | §5.3 | §5.2 | Ch6 重點2–4 |
| ⭐ Cache performance（AMAT = hit time + miss rate × miss penalty） | §5.4 | §5.3 | Ch6 重點5 |
| ⭐ Set-associative / replacement (LRU) / write policy | §5.3–5.4 | §5.2–5.3 | Ch6 重點6 |
| Multilevel cache | §5.4 內 | §5.3 內 | Ch6 重點7 |
| ⭐ 3C miss model（compulsory/capacity/conflict） | §5.8 | §5.5 | Ch6 重點13 |
| FSM cache controller | §5.9 | §5.7 | Ch6 重點14 |
| Cache coherence（snooping, MESI） | §5.10 | §5.8 | Ch8 重點5 |
| 🆕 Going Faster: cache blocking / loop tiling | §5.15 | — | — |

**讀法**：write-through vs write-back、write-allocate、AMAT 計算、3C 分類都是高頻題。🆕 **cache blocking (loop tiling)** 是 RV 版才有的知識點，M4 找不到——若題庫有，只讀 RV §5.15。

---

## H. 記憶體階層：虛擬記憶體 Virtual Memory ⭐

**✅ ISA-free，高頻。注意兩版節次順序不同。**

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| ⭐ Virtual memory, page table, page fault | §5.7 | §5.4 | Ch6 重點8 |
| ⭐ TLB（address translation 加速） | §5.7 內 | §5.4 內 | Ch6 重點9 |
| ⭐ VIPT / PIPT（cache × VM 交互） | §5.7 內 | §5.4 內 | Ch6 重點10 |
| Protection mechanism | §5.7 內 | §5.4 內 | Ch6 重點11 |
| Common framework for memory hierarchy | §5.8 | §5.5 | Ch6 重點12 |
| Virtual machines | §5.6 | §5.6 | Ch6 重點15 |

**⚠️ 節次陷阱**：M4 是 VM(§5.4) → Common Framework(§5.5) → Virtual Machines(§5.6)；**RV 把 Virtual Machines (§5.6) 排在 Virtual Memory (§5.7) 之前**，Common Framework 移到 §5.8。你按 subchapter 標考古題時這裡最容易對錯。

---

## I. 可靠度、ECC、RAID Dependability

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| 🆕 Dependable memory hierarchy（放進 Ch5） | §5.5 | — | — |
| ⭐ ECC / Hamming code (SEC/SECDED) | §5.5 | §6.2 內 | — |
| Dependability, Reliability, Availability（MTTF/MTBF/MTTR） | §5.5 | 📦 §6.2 | Ch7 重點3 |
| ⭐ RAID (0/1/5/6) | §5.11 | 📦 §6.9 | Ch7 重點4 |

**⚠️ 位置陷阱**：**ECC/Hamming 與 dependability 在 RV 版是 Ch5（記憶體章），在 M4 是 Ch6（I/O 章）。** 找同一知識點兩版跳不同章。availability 公式、Hamming SECDED bit 數計算是常見題型。

---

## J. 儲存與 I/O Storage & I/O 📦

**M4 有完整專章，RV 版拆散且縮水——這塊反而以 M4 為主。**

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| Disk / Flash storage | §5.2 內（縮） | 📦 §6.3–6.4 | Ch7 重點2 |
| Bus（synchronous/asynchronous, arbitration, bandwidth） | — | 📦 §6.5 | Ch7 重點5–8 |
| ⭐ I/O 溝通：polling / interrupt / DMA | — | 📦 §6.6 | Ch7 重點9–12 |
| I/O system performance & design | — | 📦 §6.7–6.8 | Ch7 重點13 |

**讀法**：📦 **DMA、bus arbitration、I/O system design 這些 RV 2nd 幾乎砍光**，只能看 M4 Ch6。台灣考研 **DMA / RAID 會出**，大碩 Ch7 補得比 M4 還滿——這塊建議**大碩 Ch7 + M4 Ch6 為主，RV 跳過**。

---

## K. 多處理器與平行 Multiprocessors & Parallelism ⭐

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| ⭐ Flynn taxonomy (SISD/SIMD/MIMD/SPMD) | §6.3 | §7.6 | Ch8 重點7 |
| ⭐ Hardware multithreading（fine/coarse-grained, SMT） | §6.4 | §7.5 | Ch8 重點6 |
| Multicore / shared-memory multiprocessor | §6.5 | §7.3 | Ch8 重點3 |
| Message-passing / MPP / clusters / WSC | §6.7（🆕 WSC 擴充） | §7.4 | Ch8 重點4 |
| Cache coherence（跨接 §G） | §5.10 | §5.8 | Ch8 重點5 |

**讀法**：✅ ISA-free。Flynn 分類、multithreading 三型是定義題主力。🆕 warehouse-scale computing / cloud 在 RV 版擴充。你 HPC（multi-node/InfiniBand）背景這章讀起來會很快。

---

## L. GPU 🆕⭐（你標記近年必考——重點看這區）

| 主題 | RV 2nd | M4 |
|---|---|---|
| ⭐ Intro to GPU（正文） | §6.6 | §7.7 |
| GPU system architectures | 附錄 B.2 | 附錄 A.2 |
| ⭐ Programming GPUs（CUDA model） | 附錄 B.3 | 附錄 A.3 |
| ⭐ Multithreaded multiprocessor architecture（SM, warp） | 附錄 B.4 | 附錄 A.4 |
| Parallel memory system | 附錄 B.5 | 附錄 A.5 |
| GPU floating point arithmetic | 附錄 B.6 | 附錄 A.6 |
| Real Stuff: NVIDIA GeForce 8800 | 附錄 B.7 | 附錄 A.7 |
| Mapping applications to GPUs | 附錄 B.8 | 附錄 A.8 |

**讀法**：正文只有 §6.6（RV）/ §7.7（M4）淺談，**深度全在附錄 B（RV）/ 附錄 A（M4）**。兩版 GPU 附錄內容幾乎相同（都以 GeForce 8800 為例，稍舊但觀念通用）。考點集中在 **SM (streaming multiprocessor) hierarchy、warp/block/grid、CUDA memory model、SIMT vs SIMD**——這些跟你 HPC 修過的 CUDA 直接重疊，主讀 **RV 附錄 B.3–B.4** 即可。

---

## M. 互連網路與效能模型 Interconnect & Roofline

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| Network topologies（mesh, torus, hypercube） | §6.8 | §7.8 | Ch8 重點9 |
| Cluster networking | §6.9 | — | — |
| ⭐ Roofline model | §6.10–6.11 | §7.10–7.11 | — |
| 🆕 Going Faster: multiple processors + matrix multiply | §6.12 | — | — |

**讀法**：✅ 兩版都有 Roofline（M4 在 §7.10）。topology 的 diameter / bisection bandwidth 計算是常見題。Roofline（operational intensity vs performance bound）你 HPC 報告用過，觀念熟。

---

## N. 積體電路基礎 IC Basics

| 主題 | RV 2nd | M4 | 大碩 |
|---|---|---|---|
| IC fabrication, wafer, die yield, cost | §1.5 內 | §1.7 內 | Ch9 重點1–3 |

**讀法**：很短，cost per die 與 yield 公式背起來。原文書散在 Ch1；大碩獨立成 Ch9，公式更集中，可看大碩。

---

## O. 只在 MIPS 4th、可略讀

| 主題 | M4 | 說明 |
|---|---|---|
| 📦 Assemblers, Linkers, SPIM（附錄 B） | 附錄 B | assembler/linker/loader 機制、memory usage、SPIM。RV 版整個拿掉。若考 **linker/loader 細節**才需翻 |

---

## 讀書順序建議（時間軸）

1. **地基**：A 效能 → B ISA（主讀 RV，建立 register/format 兩套對照）
2. **算術**：C（重壓 FP）
3. **處理器**：D 單週期 → F 管線（重壓 hazard；記 delay slot 版本差）→（E 多週期看考古題決定）
4. **記憶體**：G 快取 → H 虛擬記憶體 → I ECC/RAID（記位置陷阱：RV 在 Ch5、M4 在 Ch6）
5. **I/O**：J（以大碩 Ch7 + M4 Ch6 為主）
6. **平行**：K 多處理器 → L **GPU（附錄 B，你標的重點）** → M Roofline/topology
7. **收尾**：N IC → O 補漏

## 三個最容易對錯的坑（標考古題時注意）

- 🔶 **認 ISA 的題型**：只有 B 全部、F 的 control hazard（delay slot）、C 的 mult/div 介面。其餘全共用。
- ⚠️ **ECC / dependability / RAID 的章號**：RV 在 Ch5，M4 在 Ch6。
- ⚠️ **Ch5 內部順序**：RV 是 Virtual Machines(§5.6) 早於 Virtual Memory(§5.7)。

## RV-only 知識點清單（M4 找不到，別浪費時間翻）

Eight Great Ideas（§1.2）、subword parallelism（§3.6）、cache blocking / loop tiling（§5.15）、貫穿四章的 Going Faster matrix multiply（§3.8→4.12→5.15→6.12）、ARM Cortex-A53 in-order pipeline 範例（§4.11）、WSC 擴充（§6.7）。
