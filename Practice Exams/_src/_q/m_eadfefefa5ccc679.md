一、單一選擇題，共八題，每一題答對給 5 分，未答得 0 分，答錯倒扣 2 分。

2\. The following code fragments describe a solution of the bounded-buffer problem. The three variables S1, S2, and S3 are all semaphores. Suppose that the buffer initially has 10 empty slots. What are the correct initial values of the semaphores?

```c
/* Producer processes: */       /* Consumer processes: */
do {                            do {
    // produce an item              wait (S3);
                                    wait (S1);
    wait (S2);
    wait (S1);                      // remove an item from buffer

    // add the item to the buffer   signal (S1);
                                    signal (S2);
    signal (S1);
    signal (S3);                    // consume the removed item
} while (true);                 } while (true);
```

(a) S1=1; S2=1; S3=1.\
(b) S1=1; S2=0; S3=0.\
(c) S1=9; S2=1; S3=1.\
(d) S1=1; S2=10; S3=0.\
(e) S1=0; S2=10; S3=10.
