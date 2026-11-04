9\. Consider an undirected graph $G$=($V$,$E$), an edge is a relation over the vertices; the relation is reflexive, symmetric, and transitive. Computing the connected components in the $G$ is the same as to compute the equivalence classes of the vertices, $V$. Let the number of vertices be $n$ and the number of edges be $m$.

(26) Union/Find implements set operations by using forest. A set is a rooted tree where the root presents the set. Recall that there are $n$ vertices and $m$ edges. About computing the equivalence classes, which of the statement(s) is (are) true.

(a) Union operation can be done in $\Theta(1)$ time, there are at most $m$ Unions.\
(b) The time required by Find($i$) operation depends on the path length from $i$ to the root. There are at most $m$ Finds.\
(c) Applying weighting rule for Union, the time required for a Find is bounded above by O(log $n$). Applying collapsing rule for Find, the path length can be further reduced.

(A) (a) and (b) are true, but (c) is not.\
(B) (a) and (c) are true, but (b) is not.\
(C) (b) and (c) are true, but (a) is not.\
(D) all of (a), (b), and (c) are true.\
(E) Only (a) is true.
