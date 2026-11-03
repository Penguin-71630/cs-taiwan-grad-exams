2\. (17%) **Answer each of the following questions.**

(A) (3%)

Give a definition for the *reflexive transitive closure matrix* $\boldsymbol{A}^*$ of a directed graph $\boldsymbol{G}$.

(B) (3%)

What does the following function compute?

```
void Function1(int cost[][MAX_VERTICES],
                   int distance[][MAX_VERTICES], int n)
{
   /* cost is the adjacency matrix of some directed graph */
   int i, j, k;
   for (i=0; i<n; i++)
      for (j=0; j<n; j++)
         distance[i][j] = cost[i][j];

   for (k=0; k<n; k++)
      for (i=0; i<n; i++)
         for (j=0; j<n; j++)
            if (distance[i][k]+distance[k][j]<
                  distance[i][j])
               distance[i][j] =
                  distance[i][k] + distance[k][j];
}
```

(C) (3%)

Prove or disprove that a graph is bipartite only if it contains no cycles of odd length.

(D) (3%)

What is a topological sort (or topological ordering) of a directed acyclic graph?

(E) (5%)

Describe a linear time $\boldsymbol{O}(|\boldsymbol{V}|+|\boldsymbol{E}|)$ algorithm for the topological sort of a graph $\boldsymbol{G}=(\boldsymbol{V},\boldsymbol{E})$ using the depth first search implementation.
