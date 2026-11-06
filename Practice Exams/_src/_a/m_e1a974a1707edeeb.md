<!-- src: devin -->
(a) `typedef struct { semaphore mutex(1), gate(0); int count=0; } barrier;`\
`barrier_wait(barrier *b, int n) { wait(b->mutex); if (++b->count == n) signal(b->gate); else signal(b->mutex); wait(b->gate); if (--b->count == 0) signal(b->mutex); else signal(b->gate); }` (fixed $n$, reusable; semaphores permit cross-thread signaling).\
(b) Use per-file dynamic priorities based on friend/file preferences plus unbounded aging to prevent starvation; break ties by arrival time. In BBS, maintain a mutex-protected wait queue, recompute priorities at unlock, and reserve the lock for the chosen thread before signaling its private semaphore/condition variable; no kernel change is needed.
