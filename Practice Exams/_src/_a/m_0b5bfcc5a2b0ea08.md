<!-- src: devin -->
(a) fork(): vfork() is cheaper (no copy, shares address space) but suspends the parent until the child exec/exits, so the daemon cannot keep accepting requests; fork() + COW lets parent and child run concurrently\
(b) (1) Parent and child share pages marked read-only; a page is copied only when one of them writes it; (2) writable segments: data, heap, stack (text is read-only and shared anyway)\
(c) Query the OS limits, e.g. `ulimit -u` / `sysconf(_SC_CHILD_MAX)` / `/proc/sys/kernel/pid_max`, `threads-max`\
(d) Avg response (first-run) time = 249,975 ms ≈ 250 s [?] 若指 turnaround 則為 750,025 ms\
(e) Multi-level Feedback Queue\
(f) Use a multithreaded server with a pre-created thread pool (few processes × up to 100 threads) instead of one process per request, scheduled by MLFQ so short requests finish first and context-switch overhead (0.1 ms vs 1 ms) stays low
