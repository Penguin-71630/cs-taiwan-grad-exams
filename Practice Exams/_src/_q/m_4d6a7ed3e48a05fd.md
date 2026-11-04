4\. (25 points) We are given a network of $C$ cities and $R$ roads. All roads are one-way, i.e., if a road goes from city $u$ to city $v$ then there will be no roads going from $v$ to $u$. In addition, the roads will not form any *cycle*. That is, you cannot start from a city $v$, go through several cities, and go back to $v$. Finally we assume that there is a capital that can go to all other cities in the network.

We want to compute the *minimum* number of days for a tourist to go from the capital to each non-capital city. When a tourist encounters a city $v$, he will spend $c(v)>0$ days to visit all attractions in $v$. When a tourist goes from city $u$ to city $v$, he will spend $r(u,v)>0$ days on the road. Now given the $c$ function values for all cities, and $r$ function values for all roads, please compute the *minimum* number of days for a tourist to go from the capital to each non-capital city. We use $M(v)$ to denote this minimum number of days from the capital to a city $v$.

We illustrate the problem with an example of four cities $A$, $B$, $C$, $D$ and four roads. Let $A$ be the capital and $c(A)=c(B)=c(C)=c(D)=1$, and $r(A,B)=r(A,C)=r(B,D)=2$, and $r(C,D)=10$. Then $M(D)=c(A)+r(A,B)+c(B)+r(B,D)+c(D)=7$. Similarly $M(B)=M(C)=4$.

(a) (10 points) Please derive an *optimal* algorithm to compute the $M$ function for all cities other than the capital.\
(b) (15 points) Please analyze the time complexity of your algorithm and prove that it is optimal.
