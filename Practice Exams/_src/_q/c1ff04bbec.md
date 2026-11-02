9\. (10%) A benchmark is used to design a microprocessor called LHOR with five instruction classes and their dynamic statistics is as follows:

| Class | Statistics |
|:---:|:---:|
| ALU instructions | 50% |
| Loads | 20% |
| Stores | 14% |
| Branches | 12% |
| Jumps | 4% |

Two implementations are compared, i.e., the single-cycle implementation and multi-cycle implementation. The critical path, which is 60ns, exists in the Load-type instruction class for the single-cycle implementation. The multi-cycle design is done by partitioning the Load-type instruction to 6 stages, reducing the cycle period. Assume that the pipeline register introduces additional 2ns delay to each stage. Adopting the multi-cycle implementation, the number of clock cycles for each instruction class is listed as follows:

| Class | Cycles | Class | Cycles | Class | Cycles | Class | Cycles | Class | Cycles |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Loads | 6 | Stores | 5 | ALU Instructions | 4 | Branches | 4 | Jumps | 3 |

(a) (5%) What is the ratio between numbers of execution cycles for the multi-cycle implementation and the single-cycle one based on this benchmark?

(b) (5%) What is the performance speedup of the multi-cycle design?
