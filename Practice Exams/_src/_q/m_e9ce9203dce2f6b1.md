11\.

(31) Consider the following algorithm. Algorithm Sort(A, n)\
Input: Array A containing n different integer values.\
Out: Array A sorted in increasing order of values.

```
For i ← n – 1 downto 1 do {
  m ← i
      (*)
      t ← A[m];   A[m] ← A[i];   A[i] ← t // Swap A[i] and A[m]
      }
} return A
```

Which of the following instructions must be inserted at the point marked (*) so that the algorithm correctly sorts the values stored in A in increasing order of values?

(A) for j ← 0 to n – 1 do\
　　if A[j] > A[m] then　m ← j\
(B) for j ← i + 1 to n – 1 do\
　　if A[j] > A[m] then　m ← j\
(C) for j ← 0 to i – 1 do\
　　if A[j] > A[m] then　m ← j\
(D) for j ← i + 1 to n – 1 do\
　　if A[j] < A[m] then　m ← j\
(E) for j ← 0 to n – 1 do\
　　if A[j] < A[m] then　m ← j
