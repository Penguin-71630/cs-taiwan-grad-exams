注意：每大題的小題必需全對該大題才給分。每大題5分。請使用答案卡作答

1\. Suppose that we use *struct node* to represent binary trees, and use function *unknown* to process a binary tree.

```
struct node
{
  int data;
  struct node * left, * right;
};
struct node * r;
void unknown(struct node *p)
{
  struct node * q;
  if (p->left!=NULL)
    unknown(p->left);
  if (p->right!=NULL)
    unknown(p->right);
  q=p->left;
  p->left=p->right;
  p->right=q;
}
```

(2) Consider the following binary tree. After the execution of function *unknown(r)*, what is the value of the data of the rightmost node?

(A) 7\
(B) 6\
(C) 3\
(D) 2\
(E) None of the above.

<!-- fig 0.21 0.72 0.79 1.0 -->
