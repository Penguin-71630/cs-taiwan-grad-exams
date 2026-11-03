每一題組全對才計分(5 分)，答錯倒扣 1 分。每一子題均為單選題。

19\. **Problem I:** Given an integer $n \geq 2$, an $n \times n$ distance matrix of n cities, and an integer $B \geq 0$, is there a tour that visits every city exactly once and returns to the starting city by traveling within distance B?

**Problem II:** Given an undirected graph and its 2 vertices s and t, is there a path from s to t that visits every vertex exactly once?

**Problem III:** Given an undirected graph, is there a cycle that visits every vertex exactly once?

(54) Given an undirected graph G with n vertices and e a fixed positive number, consider the following possible reduction from Problem III to problem I. Let D be a distance matrix and define D[i, j]=0, if i=j; D[i, j]= 1, if (i, j) is an edge of G; D[i, j] = 2 + ne, otherwise.

Which of the followings is wrong?

(A) The above reduction is in polynomial time.\
(B) If Problem III has a satisfying cycle, then Problem I has a tour of length n.\
(C) If Problem III does not have a satisfying cycle, then Problem I has a tour of length greater than n(1+e).\
(D) The value of B in Problem I can be defined as n(1+e/2).\
(E) The above reduction can be used to show that Problem I is NP-hard.
