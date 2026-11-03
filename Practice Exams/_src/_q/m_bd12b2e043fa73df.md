C\. The following code fragments show a solution of the bounded-buffer problem. Producer processes and consumer processes share a buffer of `N` items. Items in the buffer are managed in a first-in first-out manner. A consumer removes items form the buffer, one at a time, and it waits if there is nothing in the buffer. Analogously, a producer appends items to the buffer, one at a time, and it waits if the buffer has no free space. Let `empty`, `full`, and `mutex` in the code fragments be semaphores. The buffer can store up to 10 items. Answer the following questions:

```c
/* Producer process */            /* Consumer process */
do {                              do {
   // produce an item                wait (full);
   wait (empty);                     wait (mutex);
   wait (mutex);                     // remove an item from buffer
   // append the item to the buffer  signal (mutex);
   signal (mutex);                   signal (empty);
   signal (full);                    // consume the removed item
} while (true);                   } while (true);
```

26\. What is the initial value of the semaphore `empty`?

(a) 0\
(b) 1\
(c) -1\
(d) None of the above

27\. What is the initial value of the semaphore `full`?

(a) 0\
(b) 1\
(c) -1\
(d) None of the above

28\. What is the initial value of the semaphore `mutex`?

(a) 0\
(b) 1\
(c) -1\
(d) None of the above
