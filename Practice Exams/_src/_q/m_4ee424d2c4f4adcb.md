5\. (18 points) (*Note: You do NOT need to prove the results.*) Prim's algorithm can be used for producing a minimum spanning tree. The essence of the algorithm involves greedily searching for a vertex that is connected by the lightest edge to but is not within the current tree. When running Prim's algorithm on a graph with $V$ vertices and $E=O(V^{1.5})$ edges stored with the adjacency list representation, what is the worst case asymptotic time complexity of the algorithm with respect to $V$ if

(1) (6 points) no other data structures are used\
(2) (6 points) a loser tree is used to store the vertices, where the leaves hold the smallest direct edge length to the current tree (or $\infty$ if a direct edge does not exist or the vertex is within the current tree)\
(3) (6 points) a Fibonacci heap is used to store the vertices
