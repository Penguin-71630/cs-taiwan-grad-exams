14\. (15%) The beq instruction of MIPS will cause the processor to branch to execute from a target address if the contents of the two specified registers are equal:

```
beq $rs, $rt, Target      # branch to Target if $rs == $rt
```

It uses the I-type format shown below, where *Opcode* is 6-bit wide, *rs* and *rt* are 5-bit wide, and *Immediate* has 16 bits with the leftmost bit as the sign bit.

| *Opcode* | *rs* | *rt* | *Immediate* |
|:---:|:---:|:---:|:---:|

The target address of beq is calculated as *PC + (Immediate\*4)*. Consider the pipelined implementation of the MIPS processor shown in the next page and answer the following questions.

(a) (3%) Explain the purpose of the Adder in the ID stage.\
(b) (3%) Explain the purpose of the Mux in the IF stage.\
(c) (4%) Explain the purpose of the IF.Flush control signal.\
(d) (5%) Suppose we have a *branch target buffer*, which uses PC as the input, can always predict correctly whether a branch will take, and supply the target address. Draw a diagram to explain how the IF stage may be modified. (Hint: Consider the outputs of the branch target buffer and what existing components may be removed.)

<!-- fig 0.0 0.52 1.0 1.0 -->
