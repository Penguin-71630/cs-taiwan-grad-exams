7\. (12%) In computer architectures, an operation can have several instructions for different addressing modes. For instance, Figure 1 shows four Add instructions of different addressing modes.

| Addressing mode | Example instruction | Meaning |
|:---|:---|:---|
| Immediate | `Add R4,#3` | `Regs[R4] ← Regs[R4] + 3` |
| Displacement | `Add R4,100(R1)` | `Regs[R4] ← Regs[R4] + Mem[100+Regs[R1]]` |
| Register indirect | `Add R4,(R1)` | `Regs[R4] ← Regs[R4] + Mem[Regs[R1]]` |
| Scaled | `Add R1,100(R2)[R3]` | `Regs[R1] ← Regs[R1] + Mem[100+Regs[R2] + Regs[R3]*d]` |

Figure 1: Four addressing modes for Add operation. In the Scaled addressing mode, *d* is the size of an element.

a\. (4%) Explain when to use each instruction from the high level programming language aspect.

b\. (4%) What are the advantages or disadvantages of supporting different addressing modes for the same operation in the instruction set design?

c\. (4%) Why do all the instructions in Figure 1 have at least one addend stored in registers? What would be the problems if an architecture has an instruction like

```
Add  (R1), (R2)
```

which performs Mem[Regs[R1]] ← Mem[Regs[R1]] + Mem[Regs[R2]]?
