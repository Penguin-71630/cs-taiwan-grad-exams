12\. (8%) You are using a tool that transforms machine code that is written for the MIPS ISA to code in a VLIW ISA. The VLIW ISA is identical to MIPS except that multiple instructions can be grouped together into one VLIW instruction. Up to *N* MIPS instructions can be grouped together (*N* is the machine width, which depends on the particular machine). The transformation tool can reorder MIPS instructions to fill VLIW instructions, as long as loads and stores are not reordered relative to each other (however, independent loads and stores can be placed in the same VLIW instruction). You give the tool the following MIPS program (we have numbered the instructions for reference below):

```
(01) lw   $t0 <- 0($a0)
(02) lw   $t2 <- 8($a0)
(03) lw   $t1 <- 4($a0)
(04) add  $t6 <- $t0, $t1
(05) lw   $t3 <- 12($a0)
(06) sub  $t7 <- $t1, $t2
(07) lw   $t4 <- 16($a0)
(08) lw   $t5 <- 20($a0)
(09) srlv $s2 <- $t6, $t7
(10) sub  $s1 <- $t4, $t5
(11) add  $s0 <- $t3, $t4
(12) sllv $s4 <- $t7, $s1
(13) srlv $s3 <- $t6, $s0
(14) sllv $s5 <- $s0, $s1
(15) add  $s6 <- $s3, $s4
(16) add  $s7 <- $s4, $s6
(17) srlv $t0 <- $s6, $s7
(18) srlv $t1 <- $t0, $s7
```

(a) (2%) Draw the dataflow graph of the program. Represent instructions as numbered nodes (01 – 18), and flow dependences as directed edges (arrows).

(b) (1%) When you run the tool with its settings targeted for a particular VLIW machine, you find that the resulting VLIW code has 9 VLIW instructions. What minimum value of *N* must the target VLIW machine have?

(d) (2%) Based on the code above and the minimum value of N in (b), write down the MIPS instruction numbers corresponding to each VLIW instruction in the table below. If there is more than one MIPS instruction that could be placed into a VLIW instruction, please choose the instruction that comes earliest in the original MIPS program.

| | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| VLIW Instruction 1: | | | | | | | | | | |
| VLIW Instruction 2: | | | | | | | | | | |
| VLIW Instruction 3: | | | | | | | | | | |
| VLIW Instruction 4: | | | | | | | | | | |
| VLIW Instruction 5: | | | | | | | | | | |
| VLIW Instruction 6: | | | | | | | | | | |
| VLIW Instruction 7: | | | | | | | | | | |
| VLIW Instruction 8: | | | | | | | | | | |
| VLIW Instruction 9: | | | | | | | | | | |

(e) (1%) You find that the code is still not fast enough when it runs on the VLIW machine, so you contact the VLIW machine vendor to buy a machine with a larger machine width *N*. What minimum value of *N* would yield the maximum possible performance (i.e., the fewest VLIW instructions), assuming that all MIPS instructions (and thus VLIW instructions) complete with the same fixed latency and assuming no cache misses?

(f) (2%) Write the MIPS instruction numbers corresponding to each VLIW instruction, for this optimal value of *N*. Again, as in part (c) above, pack instructions such that when more than one instruction can be placed in a given VLIW instruction, the instruction that comes first in the original MIPS code is chosen.

| | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. | MIPS Inst. No. |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| VLIW Instruction 1: | | | | | | | | | | |
| VLIW Instruction 2: | | | | | | | | | | |
| VLIW Instruction 3: | | | | | | | | | | |
| VLIW Instruction 4: | | | | | | | | | | |
| VLIW Instruction 5: | | | | | | | | | | |
| VLIW Instruction 6: | | | | | | | | | | |
| VLIW Instruction 7: | | | | | | | | | | |
| VLIW Instruction 8: | | | | | | | | | | |
| VLIW Instruction 9: | | | | | | | | | | |

> 註：原卷程式中的箭頭為「←」，此處以 `<-` 表示；小題編號原卷沒有 (c)，(f) 提到的 part (c) 照抄。
