2\. 如有運算需要，**請詳細列出完整過程**，否則不予計分。

**Section I** (40%, 10 Problems) Multiple choices— Choose all **right statements**. Each problem has four points. The score of each problem is (# of correct choices – # of wrong choices). The minimum score of each problem is 0 point.

**Problem 6 to 10**: For the rest of the problems in **Section I**, considering the code sequence, the single-cycle CPU, and the pipelined CPU figures below. For the pipelined CPU, **assume that forwarding and stalling mechanisms have been designed**.

```
1.  add  $t2, $s1, $s2
2.  sw   $s1, 0($s2)
3.  lw   $t1, 0($s1)
4.  add  $t2, $s2, $s3
5.  add  $t3, $t2, $s2
6.  lw   $t1, 0($t2)
7.  add  $t1, $t1, $s1
8.  add  $t1, $t1, $s2
9.  slt  $t2, $s2, $t1
```

<!-- fig 0.33 0.176 0.80 0.318 -->

<!-- fig 0.0 0.332 0.81 0.646 -->

<!-- fig 0.0 0.651 1.0 0.958 -->

10\. With the pipelined CPU, what control signal below will be set to 1 when the code runs to the 10^th^ cycle?

(a) RegDst\
(b) ALUSrc\
(c) MemToReg\
(d) MemWrite
