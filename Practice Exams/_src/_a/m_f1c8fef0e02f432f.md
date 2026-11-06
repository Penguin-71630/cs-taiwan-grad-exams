<!-- src: devin -->
a. VPN 17 bits, PPN 13 bits: tag array $128 \times 17 = 2176$ bits, data array $128 \times 13 = 1664$ bits (plus valid/dirty/protection bits) [?] 是否計入狀態位元依約定\
b. TLB-miss → page-table-miss (page fault); L1 events do not occur\
c. x1, x2 same block; x3 same index (0x040), different tag. 1: invalidate (P1 write hit on shared block); 2: P2 read miss, P1 writes back the dirty block, P2 loads it; 3: invalidate; 4: P2 read miss, x3 block read from memory (no write-back); 5: no bus activity (P1 hit)
