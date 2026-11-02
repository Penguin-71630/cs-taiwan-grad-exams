2\. (5 pts) A stride-based prefetching scheme exploits regular streams of memory accesses to hide memory latency. Which of the following code segments can get more benefit from stride-based prefetching? Please explain why.

Code A :

```c
int Y[100];
int i,x;
for (i= 0; i++;i:<100)
{
    Y[i]=Y[i] + x;
    x++;
}
```

Code B:

```c
struct node {
    int x;
    struct node *next;
};

while (node->next !=0) {
    node-> x = 1;
    node = node->next;
}
```

> 註：Code A 的 for 迴圈條件依原卷照錄。
