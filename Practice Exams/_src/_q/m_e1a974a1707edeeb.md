PART II – OPERATING SYSTEMS

NOTE that in the question, it is intended to provide redundant or miss certain assumption to disguise you. Please make your own assumption if necessary to answer the questions.

Bob is designing his cloud-based storage services, called BobBox and similar to Dropbox, to store the files on his desktop computer, laptop computer, and smart phones to a single cloud storage. Later, he will also open this service for his friends. Hence, the storage services will support multiple users and multiple devices. The service consists of two applications: BoxBoxClient (BBC) on the client devices and BobBoxServer (BBS) on the server. Please answer the following questions.

8\. (20 pts) Suppose a thread serves only a request. To avoid conflicted files, some file locking mechanism might be applied to block threads not holding the lock.

After the file is unlocked, all blocked threads start to compete for the lock again.

(a) [10 pts] A smart engineer designs a barrier data type of 2 semaphores and a counter and a **barrier_wait** function to help design the competing mechanism so that all threads calling **barrier_wait** will be blocked and all blocked threads will be unblocked when the number of blocked threads reaches n. Please complete the following codes for barrier and **barrier_wait** in C-like language where mutex(1) stands for the semaphore mutex is initially 1.

```c
typedef struct {
semaphore mutex(1), ...
...
} barrier;

barrier_wait (barrier *b, int n) {
...
}
```

(b) [10 pts] For the unblocked threads to compete for the lock with the most user satisfaction, especially for good friends, first come first serve might not be the best policy, however, no one would like to wait for a long time. The priority of friends might change dynamically depending on which files are requested. How do you design your scheduling policy? (5 points) How do you implement your policy? (5 points) Hint: describe which parts in the system, application, or else need to be modified. No code is needed.
