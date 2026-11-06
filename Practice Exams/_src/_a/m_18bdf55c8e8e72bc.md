<!-- src: devin -->
Maintain a bounded pool of reusable worker threads taking requests from a bounded queue; cap workers, queue length, and outstanding I/O, applying backpressure when full. This bounds thread stacks and pending work and avoids per-request thread creation.
