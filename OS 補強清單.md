# OS 補強清單 — 沒有 lab 可做、必須靠刷題補的單元

MIT 6.S081 / CMU CSAPP / NJU OS 的 lab 覆蓋的是「實作型」OS 單元（syscall、trap、page table、context switch、lock、file system、driver）。
但考研 OS 有一大塊是「給你數字算答案 / 給你狀態做判斷」的演算法題型，**這些單元沒有任何 lab 可做**，只能靠課本習題與考古題補。

本檔案把這些單元對應到 repo 內 108–115 的考古題題號，方便直接抓題來練。
題號來源為 `AI-feedback/近年考古題 - <學校>計系.md`，原題文字在 `OCR_results/` 對應檔案。

---

## 有 lab 可做的單元（不在本清單範圍）

| OS 單元 | 對應 lab |
|---|---|
| System call / user-kernel 切換 | 6.S081 Lab 1 Utilities、Lab 2 System Calls |
| Trap / Interrupt | 6.S081 Lab 4 Traps |
| Virtual Memory（頁表、位址轉換） | 6.S081 Lab 3 Page Tables |
| Demand paging / page fault handler | 6.S081 Lab 5 COW、Lab 10 Mmap |
| Thread / Context switch | 6.S081 Lab 6 Multithreading |
| Kernel 同步（lock 實作與優化） | 6.S081 Lab 8 Lock |
| File System（inode、block allocation） | 6.S081 Lab 9 File System |
| I/O 與 device driver | 6.S081 Lab 7 Network Driver |
| Process / Signal / Job control | CSAPP Shell Lab |
| 動態記憶體配置（free list、coalescing） | CSAPP Malloc Lab |
| 並行程式設計（thread pool、socket） | CSAPP Proxy Lab |
| Coroutine（context switch 本質） | NJU M2 libco |
| FAT32 檔案系統結構 | NJU M5 frecov |

---

## 1. CPU Scheduling 演算法

**為什麼沒 lab**：xv6 的 scheduler 只是最陽春的 round-robin（`kernel/proc.c` 的 `scheduler()` 就是一個 for 迴圈掃 proc table），改它學不到考題要的 Gantt chart 與平均等待時間計算。

**要練什麼**
- FCFS / SJF / SRTF / RR / Priority / MLFQ 的 Gantt chart
- Average waiting time、turnaround time、response time 計算
- Starvation 與 aging；convoy effect
- Priority inversion 與 priority inheritance
- 即時排程：EDF、Rate-Monotonic、Deadline-Monotonic 的可排程性判斷
- Linux CFS（vruntime、nice 權重）
- Solaris dispatch table（priority ↔ time quantum 反比）

**建議自寫**：50 行內的 Python 模擬器，輸入 `(arrival, burst)` 列表，輸出 FCFS / SJF / SRTF / RR 的 Gantt chart 與平均等待時間。寫過一次之後這章基本不會再算錯。

**考古題**

| 學校 | 年 | 題號 | 內容 |
|---|---|---|---|
| 台大 | 110 | Problem 3 | RR(q=3) 含 I/O burst 的 Gantt、SJF、SRTF、priority 五小題 |
| 台大 | 111 | Problem 18 | 證明 SRTF 為最小平均 turnaround 的最佳解 |
| 台大 | 113 | Problem 9 | 10 題 T/F，含 quantum 大小與 context switch overhead |
| 台大 | 113 | Problem 12 | 用 timer interrupt 實作 1ms RR scheduler（申論） |
| 台大 | 114 | Problem 7 | RR 平均 waiting time 計算 |
| 台大 | 114 | Problem 8 | Deadline-Monotonic 可排程性判斷 |
| 台大 | 115 | Problem 5 | SJF/SRTF 最佳性、EDF |
| 台大 | 115 | Problem 14 | 兩階段工作排程、最小化 makespan |
| 交大 | 108 | Problem 21 | RR(q=4) turnaround 計算 |
| 交大 | 109 | Problem 21, 22 | SRT waiting time 計算（題組） |
| 交大 | 110 | Problem 10 | Priority / MLFQ 動態調整規則 |
| 交大 | 111 | Problem 5 | 非搶佔 SJF 的 context switch 次數 |
| 交大 | 112 | Problem 7 | 由執行序列反推可能的排程演算法 |
| 交大 | 113 | Problem 4 | EDF 性質 |
| 交大 | 114 | Problem 8 | RR 性質（starvation、完成時間） |
| 交大 | 114 | Problem 9 | Linux CFS vruntime |
| 中央 | 108 | Problem 13 | 動態優先權公式（A、B 係數）推導 |
| 中央 | 108 | Problem 18 | 觸發排程的四種狀態轉換、搶佔與否 |
| 中央 | 109 | Problem 4 | 各演算法的 starvation 性質 |
| 中央 | 111 | Problem 5 | RR(q=5) 平均 waiting time |
| 中央 | 112 | Problem 17 | FCFS/SJF/RR 性質綜合判斷 |
| 中央 | 113 | Problem 17 | PCS vs SCS、priority inversion |
| 中央 | 113 | Problem 18 | RR vs FIFO turnaround、SRTF |
| 中正 | 108 | Problem 5 | Solaris dispatch table 讀表 |
| 中正 | 112 | Problem 1 | 非搶佔 SJF 平均 waiting time |
| 中正 | 113 | Problem 1 | 綜合選擇，含 convoy effect、MLFQ |
| 師大 | 108 | Problem 8 | FCFS 與 RR 平均 waiting time |
| 師大 | 109 | Problem 6 | 非搶佔 SJF |
| 師大 | 110 | Problem 2 | FCFS 與 SJF |
| 師大 | 112 | Problem 2 | SJF / RR / MLFQ 四小題 |
| 師大 | 113 | Problem 1 | Process state diagram |
| 成大 | 108 | Problem 5 | Gantt chart + interrupt latency |
| 成大 | 112 | Problem 2 | Dispatch table、time quantum |
| 清大 | 108 | Problem 2 | SRTF starvation |

---

## 2. Deadlock

**為什麼沒 lab**：xv6 用固定的 lock ordering 避免死結，沒有資源配置矩陣，Banker's Algorithm 在真實 kernel 裡根本不會被實作。

**要練什麼**
- 四個必要條件（mutual exclusion / hold and wait / no preemption / circular wait）與各自的破壞方式
- Resource Allocation Graph：單一實例 vs 多實例，cycle 是必要非充分條件
- Banker's Algorithm：Need = Max − Allocation，safety algorithm 找 safe sequence
- Resource-Request Algorithm：判斷某個請求能否被允許
- Deadlock detection（wait-for graph）vs avoidance vs prevention 的差別
- Unsafe ≠ deadlock

**建議自寫**：Banker's Algorithm 的 safety check（約 30 行），輸入 Allocation / Max / Available 矩陣，輸出 safe sequence 或 unsafe。

**考古題**

| 學校 | 年 | 題號 | 內容 |
|---|---|---|---|
| 台大 | 109 | Problem 2 | T/F，含 safe state 性質 |
| 台大 | 111 | Problem 13 | Deadlock 條件 |
| 台大 | 112 | Problem 17 | Banker's、safe sequence |
| 台大 | 113 | Problem 9 | T/F，含 safe state |
| 交大 | 108 | Problem 4 | 增加資源 / 資源種類是否維持 safe |
| 交大 | 109 | Problem 4 | Banker's 模擬找 safe sequence |
| 交大 | 111 | Problem 2 | 15 資源 4 threads 的安全性判斷 |
| 交大 | 111 | Problem 3 | semaphore 交叉持有造成 deadlock |
| 交大 | 112 | Problem 10 | Deadlock 成立條件辨析 |
| 交大 | 112 | Problem 26, 27 | 阻塞式 send/receive 造成的循環等待 |
| 交大 | 114 | Problem 5 | Banker's、safe state |
| 中央 | 108 | Problem 15 | 改變 Available/Max 後是否仍 safe |
| 中央 | 109 | Problem 11 | Banker's、wait-for graph |
| 中央 | 110 | Problem 13 | Cycle 必要非充分、unsafe 定義 |
| 中央 | 112 | Problem 11 | Avoidance vs detection 的差別 |
| 中央 | 113 | Problem 19 | Banker's 相關 |
| 中正 | 108 | Problem 2 | Unsafe 但未 deadlock 是否可能（申論） |
| 中正 | 109 | Problem 4 | Banker's 計算 Need 與 safe sequence |
| 中正 | 110 | Problem 4 | Banker's 計算 |
| 中正 | 112 | Problem 12 | 固定 lock ordering 破壞哪個條件 |
| 中正 | 112 | Problem 13 | 由 total/allocated 推 Available 並判斷可否配置 |
| 成大 | 113 | Problem 1 | Resource allocation graph |
| 成大 | 113 | Problem 3 | Banker's、safe sequence |

---

## 3. Page Replacement / Thrashing

**為什麼沒 lab**：**xv6 完全沒有 swapping**，記憶體不足就直接失敗，所以 6.S081 的 Page Tables / COW / Mmap 三個 lab 全都碰不到置換演算法。這是 OS lab 與考研之間最大的缺口。

**要練什麼**
- Reference string 模擬：FIFO / LRU / Optimal(OPT) / LFU / MFU 的 page fault 數
- Belady's anomaly（只發生在 FIFO；LRU/OPT 是 stack algorithm 不會發生）
- Clock / Second-chance / Enhanced second-chance（reference bit + modify bit 四個 class）
- Working set model、page-fault frequency、thrashing 的成因與解法
- Global vs local frame allocation；equal vs proportional allocation
- EAT（effective access time）計算：`EAT = (1−p)×memory + p×page_fault_service_time`

**建議自寫**：reference string 模擬器（FIFO / LRU / OPT 各一個函式，共約 40 行），順便驗證 Belady's anomaly（FIFO 用 3 frames vs 4 frames）。

**考古題**

| 學校 | 年 | 題號 | 內容 |
|---|---|---|---|
| 台大 | 109 | Problem 4 | Working-set model 用於 prepaging |
| 台大 | 112 | Problem 15 | Markov chain 下的期望 page fault（機率型 optimal） |
| 台大 | 114 | Problem 5 | Working-set 置換、由 hex address 抽 page number |
| 台大 | 115 | Problem 3 | Demand paging、OPT、Belady、working set、global vs local |
| 交大 | 110 | Problem 2 | LRU/OPT page fault 數、global replacement |
| 交大 | 111 | Problem 6 | Enhanced second-chance 四個 class |
| 交大 | 112 | Problem 1 | Belady's anomaly、stack algorithm |
| 交大 | 113 | Problem 23 | 二維陣列存取順序造成的 page fault 差異 |
| 中央 | 108 | Problem 16 | Reference string 模擬 FIFO/LRU/OPT |
| 中央 | 109 | Problem 7 | 同上，3 frames |
| 中央 | 110 | Problem 11 | Page size 對 page table / fragmentation 的影響 |
| 中央 | 110 | Problem 19 | LRU 模擬，求最終 frame 內容 |
| 中央 | 111 | Problem 6 | FIFO/LRU/OPT fault 數比較 |
| 中央 | 111 | Problem 19 | Local replacement、thrashing |
| 中央 | 113 | Problem 7 | Demand paging、thrashing |
| 中央 | 113 | Problem 13 | Reference string 模擬 |
| 中正 | 109 | Problem 5 | CPU 20% / disk 97.7% 判斷 thrashing 並提三種解法 |
| 中正 | 113 | Problem 3 | EAT 計算反推可容忍的 page fault rate |
| 師大 | 108 | Problem 6 | FIFO 與 LRU，4 frames |
| 師大 | 109 | Problem 7 | FIFO，5 frames |
| 師大 | 110 | Problem 5 | FIFO 與 LRU |
| 師大 | 112 | Problem 3 | LRU 逐步列出 frame 內容 |
| 成大 | 112 | Problem 4 | Demand paging、page fault rate |
| 成大 | 113 | Problem 1 | Belady、page replacement |
| 成大 | 113 | Problem 4 | 指令重啟次數、frame allocation |

---

## 4. Disk Scheduling

**為什麼沒 lab**：6.S081 Lab 9 File System 動的是 inode 與 block 配置，不碰磁頭排程；現代 SSD 也沒有 seek 的概念，所以沒有任何 lab 會教這個。但台灣考研仍然年年出。

**要練什麼**
- FCFS / SSTF / SCAN(elevator) / C-SCAN / LOOK / C-LOOK 的總磁頭移動距離計算
- 各演算法的 starvation 與 variance 性質
- Seek time + rotational latency + transfer time 的總存取時間
- CHS 定址與磁碟容量計算
- Sector sparing vs sector slipping（壞軌處理）

**注意計算細節**：SCAN 要走到磁柱端點（0 或 max）再折返，LOOK 只走到最後一個請求就折返；C-SCAN/C-LOOK 折返時「不服務」回程的請求。這是最常算錯的地方。

**考古題**

| 學校 | 年 | 題號 | 內容 |
|---|---|---|---|
| 台大 | 109 | Problem 3 | Sector sparing vs sector slipping |
| 交大 | 108 | Problem 7 | FCFS/SSTF/SCAN/LOOK 性質判斷 |
| 交大 | 110 | Problem 5 | SSTF 與 C-SCAN 服務順序 |
| 中正 | 112 | Problem 11 | CHS 容量計算 + C-SCAN 順序 |
| 中正 | 113 | Problem 1 | 綜合選擇，含 disk scheduling 與 seek time |
| 師大 | 108 | Problem 7 | FCFS 與 SSTF 總移動距離 |
| 師大 | 110 | Problem 4 | FCFS 與 SSTF，起點 cylinder 50 |
| 師大 | 111 | Problem 4 | FCFS 與 SSTF，起點 cylinder 350 |
| 成大 | 108 | Problem 4 | Seek time、rotational latency |
| 成大 | 111 | Problem 4 | C-SCAN 與 C-LOOK 移動距離 |
| 成大 | 112 | Problem 1 | Disk scheduling 綜合 |
| 成大 | 113 | Problem 5 | Disk scheduling 綜合 |

---

## 5. Classic Synchronization Problems

**為什麼沒 lab**：6.S081 Lab 8 Lock 是「優化 kernel 既有的 spinlock」（per-CPU freelist、buffer cache 分桶），不是寫 producer-consumer 或 readers-writers 的 semaphore 解。考題要的是**看懂/填空 semaphore 與 monitor 的 pseudo code**，這需要另外練。

**要練什麼**
- Critical section 三條件：mutual exclusion、progress、bounded waiting
- Peterson's solution 為何滿足三條件、為何在現代 CPU 會因 reordering 失效
- 硬體原語：test-and-set、compare-and-swap（CAS）、fetch-and-add；為何 spinlock 浪費 CPU
- Semaphore：binary vs counting；`wait()`/`signal()`（`P`/`V`）語意與初始值
- **Bounded buffer**：`empty=n`、`full=0`、`mutex=1`，以及 wait 順序顛倒為何 deadlock
- **Readers-Writers**：first（reader 優先，writer starvation）、second（writer 優先）
- **Dining Philosophers**：monitor 解的 `test()` 函式、pickup/putdown
- Monitor 與 condition variable：`wait()`/`signal()` 與 semaphore 的差別（Hoare vs Mesa 語意）
- Priority inversion 與 priority inheritance

**考題型態提醒**：交大特別愛出「給你一段 semaphore code，把 ①②③ 填空」或「指出這段 monitor code 的 bug」，所以要練到能**逐行讀**標準解法，而不是只記結論。

**考古題**

| 學校 | 年 | 題號 | 內容 |
|---|---|---|---|
| 台大 | 110 | Problem 5 | UNIX signal、`sigsuspend` 的原子性 |
| 台大 | 114 | Problem 1 | Critical-section 解法選擇 |
| 台大 | 115 | Problem 6 | Critical section 三條件、Peterson 式輪替解 |
| 交大 | 108 | Problem 3 | Readers-writers，`wrt` semaphore 行為 |
| 交大 | 109 | Problem 3 | Producer-consumer，`empty` 初始值錯誤 |
| 交大 | 109 | Problem 5 | pthread race condition |
| 交大 | 110 | Problem 24, 25 | Dining philosophers monitor 找 bug、`test()` 語意 |
| 交大 | 111 | Problem 3 | Semaphore 性質、binary semaphore 初始值 |
| 交大 | 111 | Problem 4 | Spinlock 屬 running 而非 waiting 狀態 |
| 交大 | 111 | Problem 21, 22, 23 | First readers-writers 填空題組 |
| 交大 | 112 | Problem 9 | `pthread_cond_wait` 語意 |
| 中央 | 109 | Problem 5 | Counting semaphore、critical section |
| 中央 | 110 | Problem 17 | Peterson's solution |
| 中央 | 111 | Problem 8 | Producer-consumer semaphore |
| 中央 | 112 | Problem 18 | Counting semaphore |
| 中央 | 113 | Problem 19 | Monitor |
| 中央 | 115 | Problem 19 | Semaphore |
| 中正 | 110 | Problem 1 | Condition variable、critical section |
| 中正 | 111 | Problem 1 | Test-and-set 為何浪費 CPU cycles |
| 中正 | 112 | Problem 7 | CAS 屬硬體同步原語（vs Peterson、Banker's） |
| 師大 | 108 | Problem 9 | Critical section 定義 |
| 師大 | 112 | Problem 1 | Readers-writers、condition variable |
| 師大 | 113 | Problem 2 | Critical section、busy waiting、priority inversion |
| 成大 | 109 | Problem 4 | First readers-writers 的 writer starvation、Peterson、TAS、CAS |
| 清大 | 108 | Problem 3 | 用 semaphore 實作 `acquire`/`release` |
| 清大 | 108 | Problem 7 | Race condition 辨識與修正 |

---

## 6. IPC / Message Passing

**為什麼沒 lab**：6.S081 Lab 1 有 pingpong（pipe）但只是入門；shared memory、mailbox、blocking 語意組合這些考點沒有對應 lab。

**要練什麼**
- Shared memory vs message passing 的優缺點與 system call 成本
- Ordinary pipe（單向、需親屬關係）vs named pipe / FIFO（雙向可能、不需親屬關係）
- Direct naming vs indirect naming（mailbox / port）
- Blocking vs non-blocking send/receive 四種組合，以及哪些組合會 deadlock
- 有界/無界緩衝的語意
- Microkernel 的 IPC overhead

**考古題**

| 學校 | 年 | 題號 | 內容 |
|---|---|---|---|
| 台大 | 108 | Problem 7 | Process 管理綜合，含 IPC |
| 交大 | 108 | Problem 2 | OS 基礎，含 IPC 與 system call |
| 交大 | 109 | Problem 1 | Microkernel IPC overhead、shared memory system call |
| 交大 | 110 | Problem 8 | Blocking send/receive 的先後次序 |
| 交大 | 112 | Problem 24, 25 | Direct naming vs mailbox |
| 交大 | 112 | Problem 26 | 全阻塞造成的循環 deadlock |
| 中央 | 111 | Problem 20 | Process migration、UNIX IPC |
| 中央 | 112 | Problem 12 | Ordinary pipe 單向性、named pipe 雙向 |
| 中央 | 112 | Problem 15 | Named pipe 不需親屬關係、COW |
| 中正 | 111 | Problem 1 | 綜合選擇，含 IPC 與硬體 lock |
| 成大 | 113 | Problem 2 | Named pipe |

---

## 7. Protection & Security

**為什麼沒 lab**：CSAPP Attack Lab 練的是 buffer overflow 攻擊技巧，不是考題要的 access matrix / capability / MAC 這類保護模型。

**要練什麼**
- User mode vs kernel mode、privileged instruction、protection ring
- Access matrix 及其兩種實作：access control list（按 column）vs capability list（按 row）
- Principle of least privilege、protection domain、domain switching
- setuid 與 real/effective UID、privilege escalation
- MAC vs DAC、sandboxing
- TEE / Intel SGX：enclave、remote attestation、side channel 的限制

**考古題**

| 學校 | 年 | 題號 | 內容 |
|---|---|---|---|
| 台大 | 108 | Problem 2 | TEE 適用情境 |
| 台大 | 108 | Problem 7 | Real UID vs effective UID、setuid |
| 台大 | 111 | Problem 16 | Intel SGX、remote attestation、惡意 OS 攻擊面 |
| 台大 | 115 | Problem 4 | User/kernel 隔離、MAC、sandboxing、加密 |
| 中正 | 108 | Problem 1 | 綜合選擇，含 sandbox |
| 中正 | 113 | Problem 1 | 綜合選擇，含記憶體保護與 trap |
| 成大 | 112 | Problem 1 | Capability-based protection（entitlements）、MAC |
| 成大 | 113 | Problem 2 | setuid |

---

## 建議讀法

1. **先做 6.S081 的 lab**（Page Tables → COW → Multithreading → File System），把實作型單元的理解打穩。
2. **同一時間平行刷本清單的題**。這七個單元不需要等 lab 做完，隨時可以練，而且練起來快。
3. **三個自寫模擬器**（scheduling、Banker's、page replacement）建議在讀完對應章節當天就寫完，各半小時到一小時，寫過之後計算題幾乎不會再錯。
4. **交大要特別注意倒扣**：計系全複選、答錯一個選項倒扣 2 分。上面標「性質判斷」「T/F」的題目要練到能確定每個選項的對錯，沒把握就不要選。
5. **題目原文**在 `OCR_results/近年考古題 - <學校>計系.md`，**解析與 key concept** 在 `AI-feedback/近年考古題 - <學校>計系.md`，用題號對照即可。

> 題號對照由關鍵字掃描 `AI-feedback/` 後人工篩選產生。同一題可能同時涵蓋多個單元（例如中正 113 Problem 1 是 15 小題的綜合選擇），因此會重複出現在不同段落。
