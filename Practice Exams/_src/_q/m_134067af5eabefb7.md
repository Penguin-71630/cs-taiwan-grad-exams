19\. Given a C program:

```c
#include <stdio.h>
#define BUFFER_SIZE 256
int main(int argc, char *argv[])
{
    char buffer[BUFFER_SIZE];
    if (argc < 2)
        return -1;
    else {
        strcpy(buffer, argv[1]);
        return 0
    }
}
```

(a) The program is lack of bounds checking.\
(b) Buffer-overflow vulnerability exists\
(c) The return address can be replaced\
(d) Using strncpy() in the program gives the same result as using strcpy().
