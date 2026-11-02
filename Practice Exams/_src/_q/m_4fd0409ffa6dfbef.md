單一選擇題，共 12 題，每一題答對給 4 分，未答得 0 分，答錯倒扣 1.5 分。

7\. Consider the following program:

```c
#include <stdio.h>
#define BUFFER_SIZE 256
int main(int argc, char *argv[])
{
    char buffer[BUFFER_SIZE];
    if (argc < 2)
        return -1;
    else {
        ________________; /*fill in the right instruction herein*/
        return 0;
    }
}
```

To avoid the security problem, what will be the best choice of instruction to fill in the empty slot in the program?

(a) strcopy(buffer, argv[1]);\
(b) strcopy(buffer, argv[2]);\
(c) strncpy(buffer, argv[1], sizeof(buffer));\
(d) strncpy(buffer, argv[1], sizeof(buffer)-1);\
(e) strncpy(buffer, argv[1], sizeof(buffer)+1);
