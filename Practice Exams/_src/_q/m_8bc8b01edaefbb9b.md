ARM recently built up a new CPU design center at Hsinchu in Taiwan, the first CPU design center in Asia. You are the principal engineer in a team in charge of developing a brand new CPU, called NCTU (Next-generation Compute Terabit Unit). The following what-if questions refer to some assumptions. The latencies for logic blocks in the figure are listed, while the latency of other blocks is almost negligible:

| Main control | I-mem | Adder | Registers | ALU | Sign-extend | D-mem |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 50ps | 100ps | 50ps | 40ps | 50ps | 10ps | 100ps |

The NCTU1, the basic standard 5-stage pipeline processor, is organized as the following diagram. All instructions executed by a pipelined processor are broken down as ALU: 40%, beq: 30%, lw: 25% and sw: 5%.

<!-- fig 0.0 0.325 1.0 0.776 -->

17\. Ideal execution does not exist at all. Which of following statements can be true for improving NCTU1?

(a). The pipe stages look unbalanced. The ideal CPI can be reduced to less than 1 if we move around the building blocks for better balance.\
(b). The overall performance can be always improved by making the pipeline deeper as the cycles are shorter.\
(c) Solve the load-use data hazard (load instructions followed by a dependent instruction) by inserting a hazard detection unit at the ID stage.\
(d) Increase the register file with more read ports (three reads and a write) to avoid instruction conflicts.\
(e) If ALU control decoder (marked by dashed circle) needs to take 50ps, moving the ALU control to the ID stage can improve NCTU1 for allowing more concurrent activities.
