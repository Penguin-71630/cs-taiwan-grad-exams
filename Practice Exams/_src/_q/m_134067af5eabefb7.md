一、複選題（80%），共二十題，每題全對得 4 分。答對一個選項得 1 分（答對兩個選項得 2 分，以此類推），答錯一個選項倒扣 2 分（答錯兩個選項倒扣 4 分，最多扣至該題 0 分為止），整題未作答不給分。（舉例：每題有 a、b、c、d 四個選項，某題答案為 a、b，而作答時選 a、b、c，則三個選項正確一個錯誤，該題得 3-2=1 分）請使用答案卡作答

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
