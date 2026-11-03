20\. Refer to the following functions, and function2() is invoked by thread creations:

```c
aTestFunction(char *ptr) {
    char *buffer2, *buffer=ptr;
}
int a,b,c;
int function2() {
    static int i,j,k;
    char *ptr2, *ptr = malloc(100);
    aTestFunction(ptr);
}
```

Which of the above variables are shared across threads in a multithreaded process?

(a) buffer[0] in the function aTestFunction\
(b) ptr2 in the function function2()\
(c) i,j, and k\
(d) a,b, and c\
(e) buffer2 in the function aTestFunction
