<!-- src: devin -->
a) The outcome depends on the timing/interleaving of concurrent execution accessing shared state.\
b) The alarm may expire (e.g. process preempted after alarm()) before write() starts, so the signal is lost and write() then blocks forever.\
c) (1) setjmp/longjmp (sigsetjmp/siglongjmp) out of the SIGALRM handler; (2) select()/poll() with a 3 s timeout (or non-blocking/asynchronous I/O) before write()
> 註：Drive 詳解作以 semaphore/monitor 包住 alarm 與 write，無法解決 alarm 先到期的問題，應為上述作法
