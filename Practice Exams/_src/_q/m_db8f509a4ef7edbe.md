6\. (10%) Please show the result of the following code.

```
#include <iostream>
using namespace std;

struct node {
  int value;
  struct node * next;
} n1, n2, n3, n4, n5, * f;

void foo1(struct node * p) {
  for(;p!=NULL && p->next!=NULL;p=p->next)
      if (p->value>p->next->value) {
          int t;
          t=p->value;
          p->value=p->next->value;
          p->next->value=t;
      }
}

void foo2(struct node * p) {
  struct node *q, * r;
  if (p==NULL) return;
  q=p->next; p->next=NULL;
  for(;q!=NULL;p=q,q=r) {
      r=q->next; q->next=p;
  }
  f=p;
}

int bar(struct node *p) {
  int flag, sum;
  for(flag=0,sum=0;p!=NULL;p=p->next,flag++)
      if (flag&1==1)
          sum+=p->value;
  return sum;
}

void bar2(struct node * p) {
  for(;p!=NULL;p=p->next)
      cout<<p->value<<" ";
}

int main() {
  n1.value=6; n2.value=3; n3.value=8;
  n4.value=10;    n5.value=1;
  n1.next=&n2;    n2.next=&n3;    n3.next=&n4;
  n4.next=&n5;    n5.next=NULL;
  f=&n1;
  foo1(f);
  foo2(f);
  cout << bar(f);
}
```
