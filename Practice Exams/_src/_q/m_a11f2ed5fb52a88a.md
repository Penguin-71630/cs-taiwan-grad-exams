13\. [12%] Assume a pipelined data path of a MIPS processor as shown in Figure 1.

<!-- fig 0.08 0.04 0.90 0.445 -->

Answer this problem set assuming the following instruction mix and access latency of each pipeline stage and pipeline registers:

| Add | beq | lw | Sw |
|:---:|:---:|:---:|:---:|
| 45% | 30% | 15% | 10% |

Table 1: instruction mix

| IF | ID | EX | MEM | WB | Pipeline registers |
|:---|:---|:---|:---|:---|:---|
| 110ps | 120ps | 90ps | 140ps | 60ps | 10ps |

Table 2: Pipeline latency

a\. [3%] Assuming there is no stall and that 40% of all the conditional branches are taken, in what percentage of clock cycles does the branch adder in the EX stage generate a value that is actually used?

b\. [3%] Assuming there is no stall, what is the speed-up achieved by pipelining compared to a single-cycle datapath?

c\. [2%] Assuming there is no stall, what percentages of all cycles do we use the data memory?

d\. [4%] Assume that the latency of the EX stage becomes 150 ps after adding the forwarding logics. If 20% of the instructions stall for one cycle before adopting forwarding, what percentage of stall cycles need to be eliminated by forwarding in order to get 10% speedup from adding the forward logics compared to the pipeline design without forwarding?
