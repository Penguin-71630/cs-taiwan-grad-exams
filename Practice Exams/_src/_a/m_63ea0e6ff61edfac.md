<!-- src: devin -->
NVM latency (~µs) is comparable to or smaller than the interrupt overhead (context switch, handler, cache/TLB pollution, rescheduling), so busy-polling until completion returns sooner and wastes less CPU than sleeping and being woken by an interrupt
