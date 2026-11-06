<!-- src: devin -->
(A) $A^*[i][j]=1$ iff there is a path of length $\ge 0$ from $i$ to $j$ (so $A^*[i][i]=1$), else 0\
(B) All-pairs shortest path lengths (Floyd–Warshall)\
(C) True: in a bipartite graph every edge switches sides, so any cycle returns to its side after an even number of edges\
(D) A linear ordering of vertices such that for every edge $(u,v)$, $u$ appears before $v$\
(E) Run DFS over all vertices; when a vertex finishes, insert it at the front of a list; the list is a topological order, $O(|V|+|E|)$
