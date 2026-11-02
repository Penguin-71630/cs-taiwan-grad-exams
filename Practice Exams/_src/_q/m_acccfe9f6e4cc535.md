二、複選題，共十題，每題全對得 4 分，答錯一個選項得 2 分，答錯兩個以上選項、或未答得 0 分。

17\. Select the following statements that are correct:

(a) Signature-based anti-virus software is able to detect mutated malware.\
(b) Signature-based anti-virus software is able to detect privacy stealing malware.\
(c) Cryptosystems are based on computation complexity.\
(d) Port scanning is a means for a cracker to detect a system's vulnerabilities to attack.\
(e) The following program is vulnerable to buffer-overflow attack:

```c
#include <stdio.h>
int main(int argc, char *argv[])
{
    char buffer[256];
    if (argc < 2)
        return -1;
    else {
        strcpy(buffer, argv[1]);
        return 0;
    }
}
```
