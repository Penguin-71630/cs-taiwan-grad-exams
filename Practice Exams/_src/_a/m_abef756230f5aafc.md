<!-- src: devin -->
a) The outcome depends on the timing/interleaving of concurrent execution accessing shared state.\
b) The alarm may expire (e.g. process preempted after alarm()) before write() starts, so the signal is lost and write() then blocks forever.\
c) (1) Install a SIGALRM handler that uses siglongjmp to escape to a sigsetjmp checkpoint established before arming the timer; thus expiry before write() also skips the write. (2) Make fd nonblocking and use select()/poll() in a partial-write loop with an absolute 3 s deadline, recomputing the remaining timeout after each wake-up or EINTR. Readiness alone does not guarantee that a blocking write of all 100 bytes will finish.
> 註：Drive 詳解作以 semaphore/monitor 包住 alarm 與 write，無法解決 alarm 先到期的問題，應為上述作法
