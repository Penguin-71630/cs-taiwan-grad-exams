3 Branch Prediction (8%)

For pipelined processors, control hazards could significantly decrease the performance. Dynamic branch prediction techniques have been successfully adopted in many modern processors to reduce performance penalty caused by control hazards. However, unlike direct branches (e.g. BEQ L1 in ARM or BEQ \$t0,\$t1, L1 in MIPS), indirect branches are usually difficult to predict.

A\. (2 points) Please give at least one static and one dynamic branch prediction scheme used for **direct branches** in microprocessors.

B\. (4 points) List conditions where indirect branches, instead of direct branches, are used? Which one of the listed cases is most frequent?

C\. (2 points) Please explain why indirect branches are hard to predict?
