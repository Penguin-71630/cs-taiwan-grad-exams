3\. Consider the following code of a singly linked list, with the function `F` to "rotate" the list by moving the first item of the list to the end of the list. The input to the function is the address of `first`, the pointer to the first item in the list. You need to select the correct expressions to put into the code in the following three questions so that the function works correctly.

```
struct node { int data;  struct node *next; };
void F(struct node **pfirst) {
  struct node *x, *y, *first = *pfirst;
  if (first && first->next) {
    x = first;
    y = *pfirst = ___①___;
    while (y->next) y = y->next;
    ___②___ = x;
    ___③___ = NULL;
  }
}
```

(9) What expression should be in ③?\
(A) `x`\
(B) `x->next`\
(C) `y->next`\
(D) `first`\
(E) `*pfirst`
