I. Architecture [50 %]

關於【計算機結構】的第一部分為是非題或選擇題，請利用答案紙上的**第一頁**，按照**題號順序**，標明題號，用**一行回答一題**。提供您的最終答案即可，請勿寫上計算過程。

Now, let us try to design a system using the knowledge in the computer architecture course and what we just learned from the article.

As illustrated in the article, availability and speed are well-known metrics for servers, but power consumption is becoming increasingly important. Let us consider a [big-data analysis system]{.underline} which runs the Apache Hadoop open-source software. The system is divided into two parts to handle different types of workload: (1) The data are distributed on the disks on the **Filesystem Serving nodes.** (2) The **MapReduce Computing nodes** acquire data from the Filesystem nodes and perform a MapReduce program in parallel.

The Hadoop runtime system handles the I/O details for the program, so the programmer can focus on the computation. The transactions between the Filesystem nodes and the Computing nodes are of 64MB size on average. Suppose the workloads running on the two types of nodes have the following parameters:

| Workload | User-Space Instructions per Transaction | OS Instructions per Transaction for Disk Operation | OS Instructions per Transaction for Network Operation |
|:---:|:---:|:---:|:---:|
| Hadoop MapReduce Computing | 200,000,000 | 0 | 100,000 |
| Hadoop Filesystem Serving | 100,000 | 30,000,000 | 30,000,000 |

Please answer the following questions:

9\. [3%] Suppose we build the system with Brawny cores. A Brawny Core can perform 6 billion instructions per second. Assume the disk and network operations are NOT the bottleneck. How fast can a [Brawny Core]{.underline} perform the transactions for each type of workload? (CHOOSE ONE)

(A) 30 transactions/s for MapReduce Computing, 100 transactions/s for Filesystem Serving\
(B) 30 transactions/s for MapReduce Computing, 600,000 transactions/s for Filesystem Serving\
(C) 30,000 transactions/s for MapReduce Computing, 100,000 transactions/s for Filesystem Serving\
(D) 5,000 transactions/s for MapReduce Computing, 10,000 transactions/s for Filesystem Serving

11\. [3%] Assume the Wimpy Core is capable of 2 billion instructions per second, and it does twice as much performance per watt as the Brawny Core for Filesystem Serving, but only half the performance-per-watt of the Brawny Core for MapReduce Computing. Each Wimpy chip contains 2 Wimpy cores, and each Brawny chip contains 4 Brawny cores. Consider only the power consumption of the processors, which of the following design should be the [most energy-efficient and cost-effective]{.underline}? (CHOOSE ONE)

(A) 2 Brawny chips for a MapReduce Computing node, 2 Wimpy chip for a Filesystem Serving node\
(B) 1 Brawny chip for a MapReduce Computing node, 1 Brawny chip for a Filesystem Serving node\
(C) 1 Wimpy chip for a MapReduce Computing node, 1 Brawny chip for a Filesystem Serving node\
(D) 1 Brawny chip for a MapReduce Computing node, 1 Wimpy chip for a Filesystem Serving node
