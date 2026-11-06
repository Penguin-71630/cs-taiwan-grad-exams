<!-- src: drive -->
(a) Computes the branch target address in ID (PC + Immediate×4), so a taken branch costs only 1 cycle\
(b) Selects the next PC: PC + 4 or the branch target\
(c) When the branch is taken, flushes the instruction fetched after beq (turns IF/ID into a nop)\
(d) In IF, the BTB looks up PC and outputs taken? + target; the PC mux selects BTB target or PC + 4; the ID-stage branch adder/path to the mux and IF.Flush can be removed (no misprediction)
