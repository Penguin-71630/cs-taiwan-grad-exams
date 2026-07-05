# MIT 6.S081 (Fall 2021) — Labs 摘要

> 版本：Fall 2021  
> 課程首頁：https://pdos.csail.mit.edu/6.828/2021/schedule.html  
> xv6 教科書：https://pdos.csail.mit.edu/6.828/2021/xv6/book-riscv-rev2.pdf  
> Source repo：`git clone git://g.csail.mit.edu/xv6-labs-2021`  
> 環境需求：RISC-V GNU toolchain + QEMU（任何 Linux/macOS 均可安裝）  
> 評分方式：所有 lab 均可用 `make grade` 本地自動評分，無需任何帳號。

---

## Lab 1 — Utilities (Unix 工具)

**預計時間：** 5–8 hr  
**做什麼：**
- 在 xv6 上實作 5 個 user-space 程式：
  - `sleep`：呼叫 xv6 的 `sleep` system call 暫停指定 ticks。
  - `pingpong`：父子 process 透過兩條 pipe 互傳 1 byte（練習 fork + pipe + read/write）。
  - `primes`：用 pipe + fork 實作 Sieve of Eratosthenes（Doug McIlroy 的 concurrent prime sieve）。
  - `find`：遞迴搜尋目錄樹中符合名稱的檔案（練習 directory traversal + stat）。
  - `xargs`：從 stdin 讀取每行作為額外參數呼叫子程式（練習 fork + exec + 字串解析）。

**學到什麼：** Unix system call 語意（fork, exec, pipe, wait, read, write, open, close）、process 間通訊（pipe）、file descriptor 繼承機制、遞迴目錄操作。  
**評分方式：** ✅ `make grade` 自動評分（每個程式有對應 test script）。

---

## Lab 2 — System Calls

**預計時間：** 5–8 hr  
**做什麼：**
- 在 xv6 kernel 中新增兩個 system call：
  - `trace(mask)`：追蹤指定 mask 的 syscall，每次被 trace 的 syscall return 時印出 pid、syscall name、return value。需要修改 proc struct 加入 trace mask，並在 fork 時繼承。
  - `sysinfo(struct sysinfo *)`：回傳系統狀態——空閒記憶體量（走 freelist 計算）和 process 數量（掃描 proc table 計算 state != UNUSED）。

**學到什麼：** System call 的完整實作路徑（user space → ecall → uservec → syscall dispatch → kernel function → copyout → return）、如何在 kernel 中新增 syscall（修改 syscall.h, syscall.c, usys.pl, user.h）、kernel 資料結構操作。  
**評分方式：** ✅ `make grade` 自動評分。

---

## Lab 3 — Page Tables

**預計時間：** 8–12 hr  
**做什麼：**
- **Speed up system calls**：在每個 process 的 page table 中映射一個 read-only shared page（USYSCALL），讓 `getpid()` 不需要 trap 到 kernel 就能讀取 pid。
- **Print a page table**：實作 `vmprint()` 函數，以三層樹狀格式印出 page table 的所有有效 PTE。
- **Detecting accessed pages**：實作 `pgaccess(va, npages, bitmask)` syscall，檢查指定範圍的 page 是否被存取過（讀取 PTE 的 Access bit，即 PTE_A）。

**學到什麼：** RISC-V Sv39 三級頁表結構（9+9+9+12）、PTE flags（Valid, Read, Write, Execute, User, Accessed, Dirty）、kernel 如何 walk page table（`walk()` 函數）、virtual ↔ physical address 轉換的程式實作。  
**評分方式：** ✅ `make grade` 自動評分。

---

## Lab 4 — Traps

**預計時間：** 6–10 hr  
**做什麼：**
- **RISC-V assembly**：閱讀 compiler 產生的 RISC-V 組語（call.asm），回答關於 register 用途、calling convention、endianness 的問題。
- **Backtrace**：實作 `backtrace()` 函數，沿著 frame pointer chain 印出 return address（用於 kernel panic 時的 stack trace）。
- **Alarm**：實作 `sigalarm(interval, handler)` 和 `sigreturn()` 兩個 syscall。每隔 interval 個 timer interrupt，kernel 將 user process 的 PC 導向 handler 函數；handler 完成後呼叫 sigreturn 恢復原本的 register 狀態繼續執行。

**學到什麼：** Trap 機制全流程（user → trampoline → kernel trap handler → return）、RISC-V 特權 register（sepc, stvec, sscratch）、frame pointer 和 stack frame layout、user-level signal/interrupt handling 的核心原理（保存/恢復 trapframe）。  
**評分方式：** ✅ `make grade` 自動評分。

---

## Lab 5 — Copy-on-Write Fork

**預計時間：** 8–12 hr  
**做什麼：**
- 修改 xv6 的 `fork()` 實作：不再複製父 process 的所有 physical page，而是讓父子共享同一組 physical page，將 PTE 設為 read-only + 標記 COW bit。
- 實作 COW page fault handler：當 process 嘗試寫入 COW page 時觸發 page fault，handler 分配新 physical page、複製內容、更新 PTE 為 writable。
- 實作 reference counting：每個 physical page 維護一個引用計數，只有最後一個 reference 被釋放時才真正 free。
- 處理 edge case：`copyout()`（kernel → user 複製）也需要觸發 COW、OOM 時 kill process。

**學到什麼：** Copy-on-Write 的完整實作（從 fork 到 page fault 到 page allocation）、page fault handling 流程（scause register 判斷 fault 類型）、reference counting 機制、kernel memory management 與 user page table 的互動。  
**評分方式：** ✅ `make grade` 自動評分（含 `cowtest` + `usertests`）。

---

## Lab 6 — Multithreading

**預計時間：** 5–8 hr  
**做什麼：**
- **Uthread: switching between threads**：實作用戶態 thread library 的 context switch。設計 `struct thread` 保存 callee-saved registers（ra, sp, s0–s11），撰寫 `thread_switch` 組語（和 kernel 的 `swtch` 幾乎相同）。
- **Using threads**：在一個多執行緒 hash table 程式中加入 pthread mutex lock，消除 race condition 但保持 parallelism。
- **Barrier**：用 pthread mutex + condition variable 實作 barrier（所有 thread 到齊才繼續）。

**學到什麼：** Context switch 的本質（保存/恢復 callee-saved registers + stack pointer）、user-level thread vs kernel thread 的差異、mutex lock 的正確使用（保護 critical section）、condition variable 與 barrier 同步原語。  
**評分方式：** ✅ `make grade` 自動評分。

---

## Lab 7 — Network Driver

**預計時間：** 6–10 hr  
**做什麼：**
- 為 xv6 撰寫 Intel E1000 網卡的 device driver（`e1000_transmit()` 和 `e1000_recv()`）。
- 理解 DMA ring buffer 機制：NIC 透過 DMA 直接讀寫記憶體中的 descriptor ring，driver 只需要管理 ring 的 head/tail pointer 和 descriptor 狀態。
- 處理 transmit（將 mbuf 放入 TX ring → 通知硬體 → 回收已傳送完的 descriptor）和 receive（從 RX ring 取出已收到的 packet → 交給 network stack → 補充新的 descriptor）。

**學到什麼：** Device driver 的基本架構（MMIO、DMA、interrupt handler）、ring buffer 資料結構在 I/O 中的應用、NIC 硬體如何與軟體互動（descriptor status bits）、I/O 並行性的概念。  
**評分方式：** ✅ `make grade` 自動評分（在 QEMU 模擬的 E1000 上跑 network test）。

---

## Lab 8 — Lock (Parallelism)

**預計時間：** 8–12 hr  
**做什麼：**
- **Memory allocator**：將 xv6 的全域 `kmem` free list 改成 per-CPU free list，減少 lock contention。當某個 CPU 的 free list 為空時，從其他 CPU 偷取 page（lock ordering 避免 deadlock）。
- **Buffer cache**：將 xv6 的全域 `bcache` lock 改成 hash table + per-bucket lock，減少 `bget()` 的 contention。需要實作 LRU eviction 跨 bucket 搜尋（注意 lock ordering 和 race condition）。

**學到什麼：** Lock contention 是多核效能瓶頸的主因、per-CPU 資料結構的設計模式、lock splitting / lock striping 優化技巧、lock ordering 避免 deadlock、cache/buffer 的並行化設計。  
**評分方式：** ✅ `make grade` 自動評分（含 `kalloctest` + `bcachetest`）。

---

## Lab 9 — File System

**預計時間：** 8–12 hr  
**做什麼：**
- **Large files**：修改 xv6 的 inode 結構支援 doubly-indirect block（原本只有 12 direct + 1 indirect = 最大 268 blocks；改成 11 direct + 1 indirect + 1 doubly-indirect = 最大 65803 blocks ≈ 256 MB）。
- **Symbolic links**：實作 `symlink(target, path)` system call。新增 inode type `T_SYMLINK`，將 target path 存在 inode 的 data block 中。修改 `open()` 使其追蹤 symlink（遞迴解析，設上限防止 loop），並支援 `O_NOFOLLOW` flag。

**學到什麼：** Unix 檔案系統 inode 結構（direct/indirect/doubly-indirect blocks）、block allocation 機制、symbolic link vs hard link 的差異與實作、檔案系統的層次結構（disk layer → buffer cache → logging → inode → directory → pathname → file descriptor）。  
**評分方式：** ✅ `make grade` 自動評分（含 `bigfile` + `symlinktest` + `usertests`）。

---

## Lab 10 — Mmap

**預計時間：** 10–15 hr  
**做什麼：**
- 實作 `mmap(addr, len, prot, flags, fd, offset)` 和 `munmap(addr, len)` system call。
- **Lazy mapping**：`mmap` 只記錄 VMA（Virtual Memory Area）metadata，不立即分配 physical page。
- **Page fault handler**：存取 mmap 區域時觸發 page fault，handler 分配 page + 從 file 讀入對應 block。
- **MAP_SHARED vs MAP_PRIVATE**：shared mapping 在 `munmap` 時需要 write-back dirty page 到 file；private mapping 不需要。
- 修改 `fork()` 讓子 process 繼承 mmap mapping；修改 `exit()` 自動 unmap。

**學到什麼：** Memory-mapped file 的完整實作（VMA 管理 + lazy allocation + page fault handling + write-back）、demand paging 的核心概念、virtual memory 和 file system 的交互、OS 如何用 page fault 實現各種 memory 策略。  
**評分方式：** ✅ `make grade` 自動評分（含 `mmaptest` + `usertests`）。

---

## 附錄：Lab 與考研知識點對照

| Lab | 主要對應考研知識點 | 考研相關度 |
|-----|-------------------|-----------|
| Utilities | fork/exec/pipe/wait、process 概念 | ✦✦✦✦ |
| System Calls | System call 機制、user/kernel mode 切換 | ✦✦✦✦ |
| Page Tables | 多級頁表、PTE、address translation | ✦✦✦✦✦ |
| Traps | 中斷/異常處理、trap frame、privilege level | ✦✦✦✦ |
| Copy-on-Write | COW fork、page fault handling、demand paging | ✦✦✦✦✦ |
| Multithreading | Context switch、thread、mutex、barrier | ✦✦✦✦✦ |
| Network Driver | Device driver、DMA、interrupt-driven I/O | ✦✦✦ |
| Lock | Spinlock、lock contention、parallel optimization | ✦✦✦✦ |
| File System | Inode、indirect blocks、symlink、directory | ✦✦✦✦ |
| Mmap | Memory-mapped file、VMA、lazy allocation、write-back | ✦✦✦✦✦ |
