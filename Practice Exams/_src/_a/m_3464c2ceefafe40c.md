<!-- src: devin -->
a. SMT: one core issues instructions from several hardware threads in the same cycle, sharing its functional units; multicore multithreading: each thread runs on its own core with its own execution units.\
b. i. multithreading on multicore (FP-heavy threads would contend for the same FP units under SMT)\
ii. SMT (FP and integer threads use different functional units, so they overlap well) [?] 開放題，取決於 SMT 共用功能單元的假設
> 註：Drive 詳解作 i. SMT on SMP、ii. multicore，理由未涉及功能單元共用，應為相反
