[PART I] Operating System

Bob is starting up a new computation service company to provide internet services, called *OnTime-or-Free*. The company claims that the service is charged only when the submitted computation is completed on time, i.e., 200ms or 100ms. During the Chinese New Year holiday in 2011, Bob worked in his own studio to build BCC, *Bob's Cloud Computing environment*, from scratch so as to start his own business in Spring 2011. Bob has to select the right combination for computing hardware and operating systems to provide high performance computing services with low cost. He plans to build a computer cluster; each of the computers is a commercial off-the-shelf computer and is connected to each other by computer networks.

3\. (12 pts) To prevent the processes from being blocked forever, Bob provides the following example code segment to his customers, where the *write()* function should wait only until the timer previously set by *alarm()*, i.e., 3 seconds, expires.

```c
int fd; char buffer[100];
...                     // code ignored
alarm( 3 );             // set a timer for 3 seconds
write( fd, buffer, 100 );  // write 100 bytes from buffer to the opened
                           // file descriptor fd
...                     // code ignored
```

a) (3 pts) Please define race condition.\
b) (3 pts) Please describe the cause of the race condition in the above code segment. Such race condition could block the processes forever.\
c) (6 pts) Please give two possible ways to avoid the race condition mentioned above. Your solutions must (1) prevent the processes from being blocked forever due to the *write()* function and (2) avoid polling.
