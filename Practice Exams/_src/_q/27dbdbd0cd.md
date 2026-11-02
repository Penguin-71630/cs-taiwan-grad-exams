2\. (10%) Consider a single-CPU system with the processes listed below.

| Process | Arrival Time (seconds) | *Average* Burst Time (seconds) |
|:---:|:---:|:---:|
| $P_1$ | 0 | 5 |
| $P_2$ | 10 | 4 |

Suppose both the burst time and the remaining time of each process are non-deterministic. The system runs the Shortest-*Expected*-Remaining-Time-First scheduling to allocate the CPU to processes. That is, **the CPU is allocated to the process whose *expected* remaining time is shortest among all the processes.** Suppose that the context-switch time is zero. Assume that the burst times of all these processes are *exponentially distributed* with their means shown in the above table.

Hint 1: The probability density function of an exponential random variable with mean $1/\lambda$ is $f(t) = \lambda e^{-\lambda t}$, $t \ge 0$. Its cumulative distribution function is $F(t) = 1 - e^{-\lambda t}$, $t \ge 0$.

Hint 2: A property of the exponential distribution is that it is memoryless. That is, for an exponential random variable $X$ and any positive constant $k$, $\mathrm{E}[X - k \mid X > k] = \mathrm{E}[X]$.

(a) (3%) Given that $P_1$ completes after $P_2$ arrives, what is the average waiting time of $P_1$? (The waiting time is the amount of time during which a process spends waiting in the ready queue.)

(b) (2%) Given that $P_1$ completes after $P_2$ arrives, what is the average turnaround time of $P_1$?

(c) (2%) What is the probability that $P_1$ completes after $P_2$ arrives?

(d) (3%) What is the average turnaround time for these processes?
