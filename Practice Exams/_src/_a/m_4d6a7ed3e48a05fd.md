<!-- src: devin -->
(a) Topologically sort the DAG; initialize $M(s)=c(s)$ for capital $s$ and $M(v)=\infty$ otherwise. In topological order, relax every edge $u\to v$: $M(v)\gets\min\{M(v),M(u)+r(u,v)+c(v)\}$.\
(b) $\Theta(C+R)$, optimal: all predecessors are finalized before each city; reading the roads and outputting all city distances requires $\Omega(C+R)$ time in the worst case.
