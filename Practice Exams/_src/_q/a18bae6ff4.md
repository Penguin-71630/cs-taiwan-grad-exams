14\. (8%) Given a basic five-stage pipelined MIPS CPU with comparator with the branch address computing done at the ID stage and the following sequence of instructions. We assume that branch predictor always predicts next instruction and for the execution of *#40 beq* the prediction is not taken.

```
36:  lw   $1, 8($4)        72:  lw   $4, 50($7)
40:  beq  $1, $3, 7        76:  add  $3, $4, $3
44:  and  $12, $2, $5      80:  or   $3, $2, $6
     ...                   84:  slt  $3, $6, $3
```

Please answer the following questions for execution from instruction #36 to #84.

(a) (4%) Assume there is no forwarding in this pipelined processor. How many NOPs are inserted?\
(b) (4%) Assume full forwarding. How many NOPs are inserted?
