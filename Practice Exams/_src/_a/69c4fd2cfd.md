<!-- src: devin -->
(a) $4! = 24$ outcomes but a decision tree of height 3 has only $2^3 = 8$ leaves, so ≥ 4 (in fact $\lceil \log_2 24 \rceil = 5$)\
(b) Not possible in the worst case: 5 comparisons are needed (e.g. compare a:b, c:d, the two winners, then insert the remaining element with 2 binary-search comparisons) [?] question assumes 4 suffice, but lower bound is 5
