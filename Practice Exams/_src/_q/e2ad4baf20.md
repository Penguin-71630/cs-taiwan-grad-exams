8\. (8%) Given a graph $\mathrm{G} = (\mathrm{V}, \mathrm{E})$, a subset of vertices $\mathrm{S} \subseteq \mathrm{V}$ is said to be a ***k-plex*** if the minimum degree of the subgraph induced by $\mathrm{S}$ on $\mathrm{G}$ is at least $|\mathrm{S}| - \mathrm{k}$. For example, $\mathrm{S} = \{\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{d}, \mathrm{e}\}$ is a ***3-plex*** with $|\mathrm{S}| = 5$. In contrast, $\mathrm{S}^* = \{\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{d}, \mathrm{e}, \mathrm{f}\}$ is not a ***3-plex***.

<!-- fig 0.4 0.2 0.66 0.43 -->

8-1 (4%) The ***k-plex problem*** is defined as follows: Given a graph $\mathrm{G} = (\mathrm{V}, \mathrm{E})$, positive integers $\mathrm{k}$ and $\mathrm{p}$, does $\mathrm{G}$ contain a subset of vertices $\mathrm{S}$ such that $|\mathrm{S}| = \mathrm{p}$ and $\mathrm{S}$ is a ***k-plex***? Either provide a polynomial time algorithm to solve the k-plex problem or prove that this problem is NP-hard.

8-2 (4%) Given a ***k-plex*** $\mathrm{S}$ and any nonempty subset $\mathrm{S}' \subseteq \mathrm{S}$, is $\mathrm{S}'$ also a ***k-plex***? If yes, please provide the proof. If no, please provide a counterexample.
