9\. (9%) In heap sort, functions *adjust*, *heapInitialization*, and *heapSort* (as shown below) are used. The function *adjust* starts with a binary tree whose left and right subtrees are max heaps and rearranges records so that the entire binary tree is a max heap, and the functions *heapInitialization* and *heapSort* use a series of *adjusts* to initialize the heap and perform a heap sort on a[1: n], respectively. Please analyze the complexities of:

(a) (3%) *adjust*.\
(b) (3%) *heapInitialization*.\
(c) (3%) *heapSort*.

The C declarations for heap and functions *adjust* (), *heapInitialization* (), and *heapSort* ():

```
#define SWAP (x, y, t) ((t) = (x), (x) = (y), (y) = (t))
typedef struct {
      int key
      } element;

void adjust (element a[], int root, int n)
{
  int child, rootkey;
  element temp;
  temp = a[root];
  rootkey = a[root].key;
  child = 2 * root; /*left child */
  while (child <= n) {
    if ((child < n) && (a[child].key < a[child+1].key))
      child++;
    if (rootkey > a[child].key) /* compare root and max. child */
      break;
    else {
      a[child / 2] = a[child]; /* move to parent */

      child *= 2;
    }
  }
  a[child / 2] = temp;
}

void heapInitialization (element a[], int n)
{
  int i;
  element temp;

  for (i = n/2; i > 0; i--)
    adjust (a, i, n);
}

void heapSort (element a[], int n)
{
  int i;
  element temp;

  for (i = n-1; i > 0; i--) {
    SWAP (a[1], a[i+1], temp);
    adjust (a, 1, i);
  }
}
```
