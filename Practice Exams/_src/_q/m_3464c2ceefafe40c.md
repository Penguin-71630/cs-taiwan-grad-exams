[PART I] Operating System

Bob is starting up a new computation service company to provide internet services, called *OnTime-or-Free*. The company claims that the service is charged only when the submitted computation is completed on time, i.e., 200ms or 100ms. During the Chinese New Year holiday in 2011, Bob worked in his own studio to build BCC, *Bob's Cloud Computing environment*, from scratch so as to start his own business in Spring 2011. Bob has to select the right combination for computing hardware and operating systems to provide high performance computing services with low cost. He plans to build a computer cluster; each of the computers is a commercial off-the-shelf computer and is connected to each other by computer networks.

1\. (10 pts) While choosing the processors to build the computing node, Bob has two choices: symmetric multiple processors (SMP) systems and multicore processor systems.

a\. (4 pts) Both simultaneous multithreading (SMT) on multiprocessor system and multi-threading on multicore processors provide concurrent execution for threads. Please define these two threading models.

b\. (6 pts) Suppose that each SMP processor has $K$ processors and each multicore processor has $K$ cores. Please advise Bob to select one of the above two threading models for better performance when

i\. (3 pts) more than 90% of the threads in the applications conduct floating-point computation.\
ii\. (3 pts) 50% of the threads in the applications conduct floating-point computation and the others conduct integer computation.

Please discuss your answers.
