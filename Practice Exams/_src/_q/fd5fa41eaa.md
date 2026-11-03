6\. (15%) **Answer each of the following questions.**

(A) (10%) The following algorithm takes an n by n matrix A(1:n,1:n) as input, does LU-decomposition and stores the results in the same array A(1:n,1:n), where L is a unit lower triangular matrix (the diagonal elements are all 1s, and the elements above the diagonals are all 0s) and U is an upper triangular matrix (the elements below the diagonals are all 0s). We further assume that a given matrix can be LU-decomposed in our case.

```
for i=1,2,…,n-1
   for k=i+1,…,n
      t= - A(k,i)/A(i,i);
      for j=i+1,…,n
         A(k,j)=A(k,j)+t*A(i,j);
      endfor
      A(k,i)= -t;
   endfor
endfor
```

Given a 3 by 3 matrix as stated below as an input

$$A=\begin{pmatrix} 1 & 1 & -1 \\ 2 & 4 & -1 \\ -1 & -3 & 3 \end{pmatrix}$$

What are the contents of A after implementing the algorithm? (Show integer parts only).

(B) (5%) Let $n \ge m$ be positive integers and let r be a nonnegative integers. The following algorithm will compute gcd(n,m), the greatest common divisor of n and m.

```
while (m>0) do
{r= n mod m;   n=m;   m=r;}
Return n
```

Given n=13923 and m=13056 as input, find the output of n.
