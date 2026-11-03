每一題組全對才計分(5 分)，答錯倒扣 1 分。每一子題均為單選題。

9\. Given the following graph, we intend to derive shortest paths. Since the graph has negative weights, one could have a constraint for the number of edges between the source node the destination node.

<!-- fig 0.24 0.125 0.77 0.455 -->

Assume that the start node is node 0 and one distance array is used to represent the shortest path found so far. The distance array is denoted as dist^k^, where k is the maximal number of edges between two nodes and k is the constraint for the shortest path. In other words, the value in dist^k^ is the shortest path whose number of edges is at most k. The determination of the distance array is by the following formula. Usually, one table is utilized to keep track of the determination of finding shortest path between the source node and other destination nodes. By updating the values of distances and incrementally increasing k value, one could finally have shortest paths from the source node to other destination nodes.

$$dist^k[u]=\min\{dist^{k-1}[u],\min_i\{dist^{k-1}[i]+length[i][u]\}\}$$

<!-- fig 0.0 0.765 0.81 0.945 -->

(25). What are values in distance array dist^4^[ ] ?

(A). (0, 1, 3, 5, 2)\
(B). (0, 1, 2, 3, 4)\
(C). (0, 3, 3, 5, 2)\
(D). (0, 1, 3, 5, 0)\
(E). (0, 1, 3, 5, 5).
