# CMU 15-213 (CSAPP) — Labs 摘要

> 版本：CS:APP3e (Third Edition)  
> Self-Study Handout 下載：http://csapp.cs.cmu.edu/3e/labs.html  
> 環境需求：Linux x86-64（Ubuntu 12.04+ 或相容環境）  
> 注意：交大 115 計系已出 x86 組語題，本課程所有 lab 均基於 x86-64，可同時練習 x86 指令集。

---

## Lab 1 — Data Lab

**預計時間：** 8–12 hr  
**做什麼：**
- 用極度受限的 C 子集（只能用 `!`, `~`, `&`, `^`, `|`, `+`, `<<`, `>>`，禁止 if/loop/常數>0xFF）實作 13 個 bit-level 函數。
- 範例函數：`bitXor(x,y)`（只用 `~` 和 `&` 實作 XOR）、`tmin()`（回傳 TMin）、`isPositive(x)`、`float_neg(uf)`（對 IEEE 754 取反）。
- 整數部分限制運算子數量（如 `bitCount` 最多用 40 個 ops）。
- 浮點數部分可用 if/loop 但只能用 int 運算操作 bit pattern。

**學到什麼：** Two's complement 的 bit-level 性質（取反+1、overflow 判斷、符號擴展）、IEEE 754 浮點數的 bit layout（sign/exp/frac）、不用分支的 bit manipulation 技巧。  
**評分方式：** ✅ 本地可驗證。`./dlc bits.c`（檢查是否違反 coding rules）+ `make btest && ./btest`（正確性測試）+ `./driver.pl`（評分，滿分 62）。

---

## Lab 2 — Bomb Lab

**預計時間：** 10–15 hr  
**做什麼：**
- 拿到一個 x86-64 binary bomb 執行檔，執行時要依序輸入 6 個字串（6 個 phase）。
- 輸入錯誤則 bomb 爆炸（印出 BOOM）。
- 用 `objdump -d` 反組譯 + `gdb` 設 breakpoint、追蹤 register/memory，逆向推出每個 phase 的正確輸入。
- Phase 1：字串比對；Phase 2：數列規律；Phase 3：switch/jump table；Phase 4：遞迴函數；Phase 5：字元對照表；Phase 6：鏈結串列排序。
- 隱藏 phase（secret phase）：需要在特定 phase 尾端加上觸發字串。

**學到什麼：** x86-64 組語閱讀（mov, lea, cmp, jmp, call, ret）、calling convention（rdi, rsi, rdx, rcx 傳參）、stack frame 結構、GDB 偵錯技巧（disas, x/s, ni, si, info registers）、reverse engineering 思維。  
**評分方式：** ✅ 本地可驗證。Self-study 版本已停用 grading server 通知，爆炸不扣分。6 個 phase 全部正確輸入即完成。

---

## Lab 3 — Attack Lab

**預計時間：** 8–12 hr  
**做什麼：**
- 拿到兩個有 buffer overflow 漏洞的 x86-64 target 程式（ctarget 和 rtarget）。
- **Part I — Code Injection (ctarget)**：撰寫 exploit string 覆蓋 return address，注入自己寫的 x86-64 機器碼，讓程式跳到指定函數（3 個 level，由簡入深）。
- **Part II — Return-Oriented Programming (rtarget)**：在有 stack randomization + NX bit 的環境下，用 gadget（既有程式碼片段）串接出攻擊（2 個 level）。
- 使用 `hex2raw` 工具將 hex 字串轉成 binary 輸入。

**學到什麼：** Stack layout（return address 位置）、buffer overflow 原理、x86-64 指令編碼（手寫 shellcode）、NX/ASLR 防禦機制、ROP 攻擊技巧。  
**評分方式：** ✅ 本地可驗證。用 `-q` flag 執行（跳過 grading server）：`./ctarget -q < exploit.txt`，程式印出 "PASS" 即正確。5 個 level 各有對應測試。

---

## Lab 4 — Architecture Lab (Y86-64)

**預計時間：** 12–18 hr  
**做什麼：**
- **Part A**：用 Y86-64 組語重寫三個 C 函數（linked list sum、遞迴 list copy、bubble sort），在 YAS/YIS simulator 上執行驗證。
- **Part B**：修改 SEQ（sequential）處理器的 HCL 描述，加入 `iaddq` 指令（立即數加法）。需要修改 fetch/decode/execute/memory/writeback 各 stage 的控制邏輯。
- **Part C**：在 PIPE（pipelined）處理器上優化一個 array copy 函數，目標是降低 CPE（Cycles Per Element）。可以同時修改 Y86-64 組語程式和 pipeline HCL（如加入 `iaddq`），使用 loop unrolling、減少 hazard stall 等技巧。

**學到什麼：** Y86-64 指令集架構（和 x86-64 的子集關係）、sequential CPU 的 stage 劃分、pipeline HCL 語言（控制信號描述）、pipeline hazard 的成因與解法（forwarding, stalling）、效能優化（loop unrolling 減少 branch penalty）。  
**評分方式：** ✅ 本地可驗證。Part A：`./yas prog.ys && ./yis prog.yo` 比對輸出。Part B：`make SIM=../seq/ssim TFLAGS=-i` 跑 regression test。Part C：`./benchmark.pl` 算出 CPE 分數。

---

## Lab 5 — Cache Lab

**預計時間：** 10–15 hr  
**做什麼：**
- **Part A — Cache Simulator**：用 C 實作一個通用 cache simulator，讀取 Valgrind 產生的 memory trace（格式：`L/S/M addr,size`），模擬 cache 的 hit/miss/eviction 行為。支援任意 `(s, E, b)` 參數（set index bits、associativity、block offset bits）。使用 LRU 替換策略。
- **Part B — Matrix Transpose Optimization**：優化一個 32×32、64×64、61×67 矩陣轉置函數，目標是最小化在模擬 cache（s=5, E=1, b=5，即 direct-mapped 32-set 32-byte block）上的 miss 數量。限制最多用 12 個 local variables。需要用到 blocking（分塊）技巧。

**學到什麼：** Cache 組織結構（set index / tag / block offset 的切法）、LRU 替換策略實作、AMAT 概念的直覺、cache blocking 優化技巧、如何分析 memory access pattern 的 cache 行為。  
**評分方式：** ✅ 本地可驗證。Part A：`./test-csim` 跑 8 個 trace file 比對 `csim-ref`（reference simulator）輸出。Part B：`./test-trans -M 32 -N 32` 等測試，miss 數低於閾值得分。

---

## Lab 6 — Shell Lab

**預計時間：** 10–15 hr  
**做什麼：**
- 實作一個支援 job control 的 Unix shell（`tsh`），包含：
  - 內建命令：`quit`, `jobs`, `bg <job>`, `fg <job>`。
  - 執行外部程式（fork + execve）。
  - 前景/背景執行（`&` 結尾為背景）。
  - Signal handling：正確處理 SIGCHLD（子程序結束）、SIGINT（Ctrl-C 只送給前景 job）、SIGTSTP（Ctrl-Z 暫停前景 job）。
  - 回收 zombie process（waitpid with WNOHANG | WUNTRACED）。

**學到什麼：** Unix process model（fork/exec/wait）、signal 機制（sigaction, sigprocmask）、race condition 避免（在 fork 前 block SIGCHLD）、process group 與 job control、error handling（每個 syscall 都要檢查回傳值）。  
**評分方式：** ✅ 本地可驗證。`./tshref`（reference shell）可跑相同 trace 比對輸出。`make testNN`（01–16）逐個 trace 測試。

---

## Lab 7 — Malloc Lab

**預計時間：** 20–30 hr  
**做什麼：**
- 實作 `mm_malloc`, `mm_free`, `mm_realloc`（自己的 dynamic memory allocator），取代系統的 malloc。
- 管理一塊用 `mem_sbrk()` 取得的 heap 空間。
- 需要考慮：free list 組織（implicit/explicit/segregated）、block splitting、coalescing（前後合併空閒 block）、placement policy（first fit/best fit）、header/footer metadata。
- 評分兼顧 **utilization**（空間利用率）和 **throughput**（每秒操作數）。

**學到什麼：** 動態記憶體管理的核心機制（fragmentation、coalescing、splitting）、explicit free list / segregated free list 資料結構、記憶體對齊（alignment）要求、系統程式的效能 vs. 空間 trade-off。  
**評分方式：** ✅ 本地可驗證。`./mdriver -t traces/` 跑全部 trace file，輸出 utilization 和 throughput 分數（滿分各 60%，加權合計 100 分制）。

---

## Lab 8 — Proxy Lab

**預計時間：** 15–20 hr  
**做什麼：**
- **Part I**：實作一個 sequential HTTP proxy（接受 client 連線 → 轉發 request 到 server → 回傳 response）。
- **Part II**：改成 concurrent proxy（每個連線開一個 thread 處理，或用 thread pool）。
- **Part III**：加入 LRU cache（對最近的 web object 做快取，需要用 reader-writer lock 處理 thread-safe 存取）。

**學到什麼：** Socket programming（socket, bind, listen, accept, connect）、HTTP 協議基礎（request line, headers）、concurrent programming（pthread_create, mutex, semaphore）、reader-writer lock pattern、producer-consumer pattern。  
**評分方式：** ⚠️ 無完整 autograder。提供 `tiny` web server 和 `curl` 可手動測試 proxy 功能。Self-study 以功能正確性自行驗證為主。

---

## 附錄：Lab 與考研知識點對照

| Lab | 主要對應考研知識點 | 考研相關度 |
|-----|-------------------|-----------|
| Data Lab | IEEE 754、Two's Complement、overflow | ✦✦✦✦ |
| Bomb Lab | x86-64 組語、calling convention、stack frame | ✦✦✦（交大 115 已考 x86） |
| Attack Lab | Buffer overflow、stack layout、NX/ASLR | ✦✦ |
| Architecture Lab | Pipeline datapath/control、hazard、HCL 修改 | ✦✦✦✦✦ |
| Cache Lab | Cache simulator、AMAT、blocking optimization | ✦✦✦✦✦ |
| Shell Lab | Process management、signal、fork/exec | ✦✦✦ |
| Malloc Lab | Memory management（fragmentation、allocation） | ✦✦✦ |
| Proxy Lab | Concurrent programming、socket | ✦✦ |
