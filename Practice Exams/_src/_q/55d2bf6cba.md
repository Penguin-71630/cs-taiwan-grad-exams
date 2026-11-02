12\. [10%] Answer the following questions considering a streaming application with the following address stream (byte address):

0, 4, 8, 12, 16, 20, 24, …. (i.e., 4\*n, where n= 0, 1, 2, 3…)

a\. [4%] What are the miss rates of a 32K direct-mapped cache and a two-way associate cache with a 32-byte line?

b\. [2%] What types of cache misses is this streaming application experiencing in the 3C model?

c\. [4%] Considering two mechanisms to improve cache performance, Victim Cache and Stream Buffer:

_Victim Cache:_ adopting a small fully-associative cache to store cache blocks that have been replaced from the main cache. On a cache miss, both the main cache and the victim cache are searched. A hit in the victim cache is considered as a hit and the data are moved into the main cache.

_Stream Buffer:_ prefetching sequentially adjacent cache lines into a separate buffer, when a particular cache line is brought in. If the data is found in the prefetch buffer, this is considered as a hit and moved into the cache and the next cache line is prefetched. Assume a two-entry stream buffer and assume that the cache latency is such that a cache line can be loaded before the computation on the previous cache line can be completed.

What are the cache miss rates for the Victim Cache mechanism with a 4-entry victim cache and the Stream Buffer mechanism with a two-entry stream buffer assuming a 32K direct-mapped main cache?
