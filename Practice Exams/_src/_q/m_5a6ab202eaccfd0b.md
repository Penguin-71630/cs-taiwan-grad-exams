10\. (5%)　Figure 7 presents the code for computing the number of connected components in an undirected graph. In the code, the undirected graph is stored in the form of adjacency lists. The graph has N vertices, which correspond to `vertices[N]` at Line 25. Each vertex is a `tVertex` structure as given at Line 9\~20. The function `ConnectUndirected(v1, v2)` is used for creating an undirected edge between vertex `v1` and vertex `v2`. The function `NumberOfComponents()` at Line 36 will return the number of connected components in the graph.

Please complete the code by filling the blanks in Figure 7. There are a total of **three** blanks at Line 30, 32, and 43 to be filled.

```
1   #define N 10
2
3   struct tListNode
4   {
5       int   v;
6       tListNode *pNext;
7   };
8
9   struct tVertex
10  {
11      bool visited;
12      tListNode* pAdjList;
13      tVertex() { pAdjList = 0;  visited = false;}
14
15      void Connect (int v)
16      {
17          tListNode *pNeighbor = new tListNode;
18          pNeighbor->v = v;
19          pNeighbor->pNext = pAdjList;
20          pAdjList = pNeighbor;
21      }
22
23  };
24
25  tVertex vertices[N];
26
27  void DFS (int v)
28  {
29      tListNode *pN;
30      vertices[v].visited = ____________;
31
32      for ( pN = vertices[v].pAdjList; pN ;____________)
33          if ( !vertices[pN->v].visited ) {   DFS( pN->v); }
34  }
35
36  int NumberOfComponents ()
37  {
38      int k;
39      int cnt = 0;
40
41      for ( k = [?]; k < N; k++)    vertices[k].visited = false;
42      for ( k = 0; k < N; k++) {
43          if ( !vertices[k].visited ) { ____________  }
44      }
45      return cnt;
46  }
47
48  void ConnectUndirected(int v1, int v2)
49  {
50      vertices[v1].Connect (v2);  vertices[v2].Connect (v1);
51  }
```

Figure 7. Code for computing the number of connected components of an undirected graph
