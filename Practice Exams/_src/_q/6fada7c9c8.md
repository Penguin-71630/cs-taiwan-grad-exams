7\. (10%) Suppose that there are a number of processes, $P_1, P_2, \ldots$, in a computer. Their arrival times are denoted by $a_1, a_2, \ldots$; their CPU burst times are denoted by $b_1, b_2, \ldots$. Processes are scheduled by the *Shortest-Remaining-Time-First scheduling* algorithm. Suppose that the context switching takes 0 second.

(a) Consider the case with 2 processes where $a_1 = 0$, $b_1 = 10$, $a_2 = 4$, and $b_2 = 2$. In this case, what is the total waiting time (over all the processes)? (5%)

PS: Waiting time of a process is the sum of the periods spent waiting in the ready queue.

(b) Consider the case with $n$ processes. For each process $i$, $a_i < a_{i+1} < a_i + b_i$ and $b_i < b_{i+1}$. Write the total waiting time (over all the processes) in terms of $a_1, a_2, \ldots, a_n$ and $b_1, b_2, \ldots, b_n$. (5%)
