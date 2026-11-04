10\. For a doubly-linked list class, each of its nodes has two links `left` and `right` to its two neighboring nodes. Assume that we want to implement a member function `ShiftRight`, which takes an input `x`, a pointer to a node, and swaps that node with the node to its right. Let us further assume that neither `x` nor the node to its right is the first or the last node of the list. There are six pointers to be set, and the statements, labeled `s1` to `s6`, are listed in the box below. Which of the following ordering of these statements will produce the correct behavior?

```
if (x && x->right && x->right->right && x->left) {
  DoublyLinkedListNode<T> *y = x->right;
  x->left->right = y;       // s1
  x->left = y;              // s2
  y->right->left = x;       // s3
  x->right = y->right;      // s4
  y->right = x;             // s5
  y->left = x->left;        // s6
}
```

(A) s5→s2→s6→s1→s4→s3\
(B) s2→s5→s4→s3→s1→s6\
(C) s4→s3→s6→s1→s2→s5\
(D) s1→s2→s3→s6→s5→s4\
(E) s4→s5→s3→s6→s1→s2
