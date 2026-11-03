每一題組全對才計分(5 分)，答錯倒扣 1 分。每一子題均為單選題。

12\. Algorithm K is as follows.

Input: G = (V,E), a connected undirected weighted graph with n vertices.\
Output: G'= (V, E'), a minimum weight spanning tree (also known as minimum spanning tree), where E' is a subset of E and spans every vertex in V.\
Initially E' is empty set.\
Repeat the following two steps until (V, E') becomes a tree:\
Step 1: Select one edge in E (and not in E') that does not form a cycle with those already in E' and is of the lowest weight among all such edges. Name the selected edge $e_i$.\
Step 2: $E' := E' \cup \{e_i\}$.

(33). Which of the following statements about algorithm K is wrong?

(A) The output of K is a spanning tree.\
(B) The output of K is a graph with n-1 edges.\
(C) The output of K is a tree with minimum weight among all spanning trees of G.\
(D) The output of K is a spanning tree only if no pair of edges in E are of the same weight.\
(E) The output of K is a tree with minimum weight among all spanning trees of G even if some pairs of edges in E are of the same weight.
