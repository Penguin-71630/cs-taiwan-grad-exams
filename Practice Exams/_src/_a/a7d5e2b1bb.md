<!-- src: devin -->
(a) Immediate: constants; Displacement: local variables / struct fields; Register indirect: pointer dereference; Scaled: array indexing a[i]\
(b) Adv: fewer instructions, smaller code, easier compilation; Disadv: more opcodes/complex decoding and hardware, variable instruction length/CPI, harder to pipeline\
(c) Registers are fast and need few encoding bits; mem-mem Add needs 3 memory accesses per instruction, longer encoding, slower and complicates pipelining (variable latency, structural hazards on memory)
