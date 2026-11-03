4\. Consider the following program. Please answer the following questions.

```
#include <stdio.h>
int data[]={8, 26, 5,77,1,61,11, 60, 15, 49, 19};
int n=10;
void a(int r)
{
  int e, j;
  e=data[r];
  for(j=2*r;j<=n;j*=2)  {
    if (j<n&&data[j]<data[j+1]) j++;
    if (e>=data[j]) break;
    data[j/2]=data[j];
  }
  data[j/2]=e;
}
int main(void)
{
  int i;
  for(i=n/2;i>=1;i--)
    a(i);
}
```

(10) What is the result of *data[10]*?

(A) 11\
(B) 1\
(C) 15\
(D) 26\
(E) None of the above
