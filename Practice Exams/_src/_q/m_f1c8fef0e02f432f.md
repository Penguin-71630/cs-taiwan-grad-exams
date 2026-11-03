[PART II] Computer Architecture

Note: [Part II]題目，請務必算出答案，勿只列式子，若無法整除，算至小數後第一位（採四捨五入）

6\. (20 pts) You are given a bus-based multiprocessor system which implements a snooping-based cache coherency protocol. There are two processors P1, P2 in the system. Each processor has its own L1 cache. The memory system specification is given below:

- L1 Cache: physical addressed, 64KB, direct-mapped, 32B block size, write-back cache
- Virtual Memory: 8K page, 1 GB virtual address space
- TLB: fully associative, 128 entries
- 64 MB of addressable physical memory.

x1, x2, and x3 represent one-word variables. The physical addresses (represented in hex) of x1, x2 and x3 are 0x00AF0804, 0x00AF0808, and 0x00AE0804, respectively. Answer the following questions considering the possible events: TLB-hit/miss, page-table hit/miss, L1-hit/miss, write-back, invalidate.

a\. (3 pts) What are the sizes of the tag and data arrays of the TLB?\
b\. (2 pts) Please write down the correct order of the events listed above for detecting a page fault. Note that some events may not occur.\
c\. (15 pts) Assume TLB hits for all the memory requests. X1 and x2 are in the L1 caches of P1 and P2. Show the bus activities for each memory request.

| Time | P1 | P2 | Bus activity |
|:---|:---|:---|:---|
| 1 | Write x1 | | |
| 2 | | Read x2 | |
| 3 | Write x1 | | |
| 4 | | Read x3 | |
| 5 | Read x2 | | |
