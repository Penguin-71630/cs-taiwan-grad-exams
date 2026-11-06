<!-- src: devin -->
Use topological-order DP: $d[v,i,j]$ is the minimum distance from A to $v$ using exactly $i$ thick and $j$ thin edges; initialize $d[A,0,0]=0$, all others $\infty$. Relax each edge, incrementing its corresponding count and retaining predecessor states; return $d[F,k,n]$ and reconstruct the path (or report none). Acyclicity prevents repeated vertices.\
Time $O((N+M)(k+1)(n+1))$; space $O(N(k+1)(n+1)+M)$. Reject immediately if $k+n>N-1$.
