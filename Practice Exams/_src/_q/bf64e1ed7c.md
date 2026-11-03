4\. (20 points) Find a shortest path in a DAG with given constraints. A graph is a *DAG* if it is *directed* and it has *no* cycle. Every edge has a positive integer distance, and is either *thick* or *thin.* Figure 2 illustrates such a DAG. For example, the edge from A to B is thick and with a distance 1, and the edge from A to C is thin and has a distance 2.

<!-- fig 0.37 0.15 0.64 0.60 -->

Now given nodes A and F, and two integers $k$, $n$, find the shortest path from A to F that goes through exactly $k$ thick edges and $n$ thin edges, and does not go through any node twice. For example, the shortest distance from A to F that goes through two thick and two thin edges is 15 by going through A-B-C-E-F. The path A-C-E-F is not a valid solution because it only goes through one thick edge. The path A-B-D-E-F does go through the right number of edges, but its total distance is 25, which is not the minimum.

Please describe the key ideas in your algorithm *without using pseudo code.* Finally analyze the time complexity of your algorithm. We assume that there are $N$ nodes and $M$ edges in the DAG.

**Your entire description and analysis can only use at most *400* Chinese characters or *400* English words. *Over-sized description or analysis will be ignored. Pseudo code will also be ignored.***
