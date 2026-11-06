<!-- src: devin -->
(a) 7 (lw→beq 2 + beq mispredict flush 1 + lw→add 2 + or→slt 2) [?] counts the flushed `and` as a NOP; 6 if not counted\
(b) 4 (lw→beq 2 + flush 1 + lw→add 1) [?] 3 if the flush is not counted
