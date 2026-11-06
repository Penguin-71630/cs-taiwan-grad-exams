# Answer quality review

Branch: devin/1793966693-answers. No branch switch, commit or push. Report is outside repository.

Final census includes all 60 newly merged answers from b-05/38/39: **1,053 unique answer files**. Source markers unchanged. All 28 files with > 註 were reviewed, including newly merged multiplication question. The new batches are included in the full counts and uncertainty registry; the numerical sample is fixed.

## (a) Counts by source

| Source | Unique files |
|---|---:|
| official | 462 |
| drive | 165 |
| devin | 426 |
| **Total** | **1053** |

**58 [?] files** ({'devin': 55, 'official': 2, 'drive': 1}); **28 annotated files** ({'devin': 13, 'official': 14, 'drive': 1}). Counts are unique files/IDs, not topic occurrences or grouped subquestions.

## (b) Complete uncertainty registry

All literal [?] files, including new batches. Reasons below are recorded caveats, not a claim all 58 flagged answers were independently solved. All subpart caveats included.

| ID | Year / school / paper / question | Source | Reason |
|---|---|---|---|
| 144e766d3e | 101 台大《計算機系統》Q2 | devin | 假設每個目錄僅一個 data block |
| 3703ca2ea0 | 105 台大《資料結構與演算法》Q3 | devin | recursion depth about $\log_m n$; may be intended as $O(1)$ |
| 378d21c6e8 | 105 清大《計算機系統》Q11 | devin | linked allocation is also defensible if a tail pointer is kept |
| 3a18d18414 | 104 清大《計算機系統》Q13 | devin | number of banks unspecified; Drive 詳解 assumes 4 banks: $89/29 \approx 3.07$ |
| 4109c4df50 | 103 清大《基礎計算機科學》Q6 | devin | open-ended design question |
| 42d8af50b3 | 103 清大《基礎計算機科學》Q5 | devin | open-ended design question |
| 556601e5e2 | 102 台大《資料結構與演算法》Q2 | devin | other single rotations/colorings are also valid, e.g. left-rotate at 4: 2B(1B, 6R(4B(3R, 5R), 8B(7R, NIL))) |
| 5c377025a5 | 103 台大《數學》Q8 | devin | Two blanks do not exhaust the possible dimensions. |
| 69c4fd2cfd | 104 清大《基礎計算機科學》Q11 | devin | question assumes 4 suffice, but lower bound is 5 |
| 80c9b85bcb | 102 清大《計算機系統》Q12 | devin | 依 IBM base-16 格式（0.hhhhhh × $16^{E-64}$，首 hex digit 非 0）作答；題目所稱 hidden 1 在 base 16 下無法表示 A，故未採用 |
| a18bae6ff4 | 103 清大《計算機系統》Q14 | devin | counts the flushed `and` as a NOP; 6 if not counted / 3 if the flush is not counted |
| a2198b823f | 103 台大《計算機結構與作業系統》Q6 | devin | Network latency is unspecified; its position relative to local storage is not universal. |
| a650a220e6 | 107 清大《計算機系統》Q10 | devin | store fraction not given, extra write-through stalls on write hits not counted |
| b6b7a9ae69 | 106 台大《數學》Q2 | devin | 字面上 $k=1$ 平凡成立，題意應為 $k \geq 2$ |
| c8a0b207cf | 101 清大《計算機系統》Q3 | devin | This is not a bound on the number of smaller segments; the maximum segment count requires a minimum segment size or a segment-selector width, neither of which is specified. |
| cc36194f12 | 103 清大《基礎計算機科學》Q9 | devin | as upper bounds (B)(C)(D) are also true / DP is $O(nW)$, pseudo-polynomial (exponential in input size); the decision version is NP-complete |
| cd21a936c0 | 106 台大《計算機系統》Q4 | devin | VLIW 主要利用 ILP，是否算有效可辯 |
| d683546f3a | 104 清大《基礎計算機科學》Q13 | devin | sampling mode unspecified |
| de67dab11b | 102 清大《計算機系統》Q8 | devin | 亦有答 interrupt-driven 者 / Reboot 與 Overheat 先後各書不一 |
| dm03_519807ce99a61a9d | 107 交大《數學》Q15 | devin | 依 (3) 中 $c_{32}, c_{13}, c_{23}$ 的取法而定 |
| e384e8ffd1 | 100 清大《計算機系統》Q7 | devin | open-ended; indexed with justification may also be accepted |
| e9fe4a8835 | 107 清大《計算機系統》Q1 | devin | Assumes concurrent I/O and FIFO wake-up insertion; the common round-based estimate $15/16.1 \approx 93.2\%$ assumes all ten I/O-bound tasks run between CPU-bound quanta, which does not describe this steady-state queue. |
| f03bcb93dc | 101 台大《計算機系統》Q3 | devin | 開放題 |
| fba5763d8f | 106 清大《計算機系統》Q3 | devin | 依所採 Stallings 單一 suspend 模型 |
| m_0131db6bb269c7ec | 106 交大《數學》Q11 | devin | fails for trivial $P = I$ or $P = 0$ (only one eigenspace), or if the projection is not orthogonal |
| m_04fbb0ca028a7ae3 | 102 交大《資料結構與演算法》Q18 | devin | Assumes a full binary tree; if unary internal nodes are allowed, arbitrarily long unary chains make the objective approach $0$, so no minimum exists. |
| m_0a1e04bc48e289c2 | 101 台大《計算機系統》II-Q3 | devin | DRAM/disk 延遲需自行假設 / 每 rack 伺服器數未給 / 開放題 |
| m_0b5bfcc5a2b0ea08 | 102 台大《計算機系統》Q15 | devin | 若指 turnaround 則為 750,025 ms |
| m_1d0c7004007a2987 | 107 台大《計算機系統》Q2 | devin | 無官方或 Drive 解答，估算假設可有不同解讀 |
| m_269a7594003eea9e | 104 交大《計算機系統》Q24-Q28 | official | 題目 X/4 疑為筆誤 |
| m_2bdb60cbb6f7c8a0 | 103 台大《數學》Q7 | devin | Literal property (b) alone does not ensure uniqueness; the candidate must also contain $S$. |
| m_2c638accd883540b | 106 台大《計算機系統》Q9 | devin | 開放題 |
| m_31bffc4aa1f14a4b | 104 台大《資料結構與演算法》Q1 | devin | > 註：Drive 網友作 (4)A (6)A (9)A；但依 index 插入/刪除須先走訪 $O(n)$，單向串列刪 p 需找前驅（p 為尾端時無法用複製下一節點技巧） |
| m_3464c2ceefafe40c | 100 台大《計算機系統》Q1 | devin | 開放題，取決於 SMT 共用功能單元的假設 |
| m_35d5371a97fa8772 | 103 台大《計算機結構與作業系統》Q13 | devin | No component timings are given, so a numerical minimum cannot be determined. |
| m_3b60bb957f31bd01 | 107 台大《資料結構與演算法》Q11 | devin | Assumes an unsuccessful search ($13/5=2.6$ comparisons); the question does not specify whether the key is present. |
| m_3e3e351d3728fcc9 | 105 台大《計算機結構與作業系統》Q6 | devin | If “buffered/unbuffered libraries” means stdio versus read/write, both use the page cache; stdio adds a user-space buffer, giving two versus one CPU copies instead. |
| m_4ad6808ea1d03e97 | 105 台大《計算機結構與作業系統》Q1 | devin | Transfer aggregation is unspecified. / Float width and transfer model are unspecified. / Idealized continuous-work limit; topology is unspecified and fixed $N$ caps useful parallelism. |
| m_4ee424d2c4f4adcb | 104 台大《資料結構與演算法》Q5 | devin | 每回合掃整個 adjacency list $O(E)$ 共 $V$ 回；若允許 key/visited 陣列則為 $O(V^2)$（部分解答作此） |
| m_536cb2270e631b24 | 107 清大《基礎計算機科學》Q7 | devin | unclear whether the original tree or the post-deletion tree is meant; after deletion: 30B(20B(-, 25R), 40R(36B(35R, 37R), 45B)) |
| m_54a48fde953563f8 | 101 台大《計算機系統》II-Q2 | devin | 題目未給 store 比例，題意不明 / 假設 30% loads/stores 皆計入 dcache stall |
| m_57d966568d3767c3 | 105 台大《數學》Q3 | devin | (C) is also true if “orthogonal set” is defined to exclude the zero vector; that convention is unspecified. |
| m_5fe7ceb2146da109 | 100 交大《計算機組織》II-Q4 | devin | 未計暫存器寫入時間（依常見教科書算法） |
| m_750db06da9154914 | 107 台大《資料結構與演算法》Q4 | devin | Standard sift-down bound; the input distribution and starting node for the expected time are unspecified. |
| m_816db793ff11023a | 105 交大《數學》Q6 | devin | 依 $P_n$ 定義而異：次數 $<n$ 時 rank $=n-1$ (F)；次數 $\le n$ 時 rank $=n$ (T) |
| m_894ed0ea2e4fb774 | 102 台大《計算機系統》Q7 | devin | 題意不明；依圖每單位工作成本 WCS/BCS = 1.2/1.35 ≈ 0.9，且 WCS 耗電較少 |
| m_8d43d01ae64bd3e5 | 107 交大《數學》Q10 | devin | 題意為「RREF 須滿足的條件」；(1) 若照字面「所有非零元皆為 1」則為 F |
| m_aa100b8eb21d0707 | 100 台大《計算機系統》Q7 | devin | (F) 動態分支預測只降低 control hazard 的 penalty，是否算 resolved 可辯 |
| m_af11eb37e2e74bf7 | 103 交大《資料結構與演算法》Q8 | devin | Drive solutions disagree: (C) greedy versus (D) augmenting-path method. |
| m_bf1a11c69b44dabc | 101 清大《計算機系統》Q9 | devin | in this figure the MemtoReg mux's 0 input is Read data (in the textbook it is 1) |
| m_c27a9f5a16cc1d8f | 102 交大《資料結構與演算法》Q7 | drive | The seven-rotation sequence is not defined: left_rotate(1) has no right child. If invalid rotations are treated as no-ops, the inorder sequence is 1 2 3 4 5 6 7. |
| m_cd774270964414f4 | 104 台大《計算機系統》Q5 | devin | 若隨核數增大 N 則屬 weak scaling |
| m_cec03837d66daa73 | 102 交大《計算機系統》Q19 | official | > 註：依題設延遲自算 p/g 2 + 群組 G/P 3 + 第二層進位 3 + 組內進位 3 + sum XOR 2 = 13（非 12），(E) 存疑 |
| m_d5f3c6ae448ee229 | 104 台大《計算機系統》Q4 | devin | 假設 critical word 為 4 B |
| m_d80b42f259568b8a | 104 台大《計算機系統》Q8 | devin | 開放題，此為一種解法 |
| m_ed05c274974a7772 | 107 台大《資料結構與演算法》Q14 | devin | Uses the inorder successor; replacing by the predecessor instead gives (C), and the deletion convention is unspecified. |
| m_f1c8fef0e02f432f | 100 台大《計算機系統》Q6 | devin | 是否計入狀態位元依約定 |
| m_f4112a66ac5dac1e | 102 交大《資料結構與演算法》Q3 | devin | 程式題，僅給演算法要點 |

## (c) All annotated disagreements and verdicts

The shorthand 'official disagreements' includes **14 official-key notes, 13 Devin-vs-Drive notes, and 1 Drive note**. Every > 註 file appears once. Official answer bodies remain keyed even where the mathematical verdict disagrees; only official notes were edited.

Question Markdown was read for every ID. Four diagram-dependent figures were read from existing topic PDFs: flow, BST rotations, multiplier, and pipeline control wiring. Image URL downloads returned HTTP 403; existing PDF figures provided the needed evidence. Independent Python corroboration: ~/keys-raw/check_disagreements.py and disagreement-computations.json. Hardware/wording assumptions are explicit below.

| ID | Year / school / paper / question | Source | Verdict |
|---|---|---|---|
| 5c377025a5 | 103 台大《數學》Q8 | devin | Supported. Intersection dimensions 0–5 are all possible for distinct subspaces of a six-dimensional space, not just two universal values. Complex dimension in (c) is 28; underlying real dimension is 56. Equality of dimension numbers over different fields does not establish the claimed real-space isomorphism. In (d), 'n rows' should read columns; rank is m. |
| f6b69f2d1a | 102 清大《基礎計算機科學》Q6 | devin | Supported. Cholesky gives lower rows [3,0,0], [1,4,0], [-1,1,5]; retain original upper entries in the in-place array. Independently ord_11(3)=5, ord_31(3)=30, and 3^5 mod31=26. |
| m_04fbb0ca028a7ae3 | 102 交大《資料結構與演算法》Q18 | devin | Supported under the full-tree assumption. Exhaustive subset DP over all labeled full binary trees gives 3/4, not the sum 91/32. Corrected the child's full-tree explanation 'all six at depth 3': weights 2,3 at depth 2 and 4,4,5,6 at depth 3 achieve the value. Added [?]: if unary chains are allowed by 'binary tree', the infimum is 0 and no minimum exists. Largest-first max/2 merging is valid for full trees by exchanging largest weights into deepest sibling positions. |
| m_1367abc6ef8f1b1e | 102 交大《資料結構與演算法》Q12 | devin | Supported as a standard Kruskal bound. Counting sort is O(E+V); union-find then costs O(E alpha(V)). Connectedness absorbs V. O(V log V) alone neglects potentially dense edge input. This is a valid bound, not a claim that all MST algorithms require it. |
| m_14f1517f250fc954 | 100 交大《作業系統》Q16 | official | Supported. Row-major sequential writes cause 100 faults/10,000 accesses, with 1 s disk service. EAT is 109.9 us (110 us if fault service is added to each base access), not 1.01 us. Only B is correct; official B,C retained. |
| m_269a7594003eea9e | 104 交大《計算機系統》Q24-Q28 | official | Supported. LRU simulation filling frames 0,1,2 in order ends with pages [0,3,1]; final X=1375=0x55F, base-5 21000. X/4=343.75 cannot equal an integer base-5 digit expansion. Official digits represent X, not X/4. Frame-allocation convention is assumed as usual; the noninteger-offset issue survives any frame assignment. |
| m_2bdb60cbb6f7c8a0 | 103 台大《數學》Q7 | devin | Supported literally. Property (b) alone is also satisfied by {0}, so it cannot establish uniqueness unless the candidate subspace must contain S. For S empty, positive-number-of-summands excludes every vector, so an empty-sum convention is required. Child supplies the corrected smallest-containing-subspace theorem. |
| m_31bffc4aa1f14a4b | 104 台大《資料結構與演算法》Q1 | devin | Supported. Insertion/deletion by index in a singly linked list includes O(n) traversal. Pointer-based removal still needs a predecessor in the general case, especially for the tail. Doubly linked pointer-based removal is O(1). The child's A,B,B,B,B,B,B,B,B,A sequence is correct for stated worst cases. |
| m_3464c2ceefafe40c | 100 台大《計算機系統》Q1 | devin | Only conditionally supported. Shared FP units explain preferring independent cores for FP-heavy threads, and mixed integer/FP threads may exploit SMT. But SMP processor resource counts and per-thread throughput are unspecified; percentages alone cannot select a universal winner. Softened the categorical reversal of Drive; [?] retained. |
| m_3e269d668e0fdd3e | 101 交大《作業系統》Q36-Q38 | official | Supported, with stronger wording needed. main joins tid3 but not the final tid2 created by tid3. Even assuming atomic strcat, final b may be printed or not (2 or 3). Actual unsynchronized strcat/printf buffer access is a C/POSIX data race/undefined behavior, not a guarantee of just two possible counts. Expanded note; official grouped letters unchanged. |
| m_42849f2fda025bc4 | 103 交大《離散數學與線性代數》Q9(b) | devin | Supported. In the positive-integer universe Goldbach concerns even n>2. The multiplicative prime predicate must exclude 1. Child's even-not-2 antecedent and not-1 primality definition supply both missing restrictions. |
| m_512a99a3f1f298f9 | 101 交大《數學》Q3 | official | Supported. At a=5,b=2, rank(A)=rank(B)=rank(AB)=2, hence N(AB)=N(B) and C(AB)=C(A), contradicting the only-if parts of A,B. The fixed leading 2x2 minor of AB equals 4, excluding rank 1. Rank 2 also occurs with just one singular factor, excluding D. Only E is universal; official A,B,E retained. |
| m_5a6b54660e48f655 | 103 交大《計算機系統》Q5 | official | Supported. Read multiplier figure: B has a 32-bit multiplicand and 64-bit combined product/multiplier register; arithmetic updates its upper half with a 32-bit adder/subtractor. D's 'has to be a 64-bit adder' is false too, alongside B's logical-shift claim for signed Booth multiplication. Official B retained. |
| m_6f7fef327f047a75 | 100 交大《作業系統》Q14 | official | Supported under after-grant interpretation. All C,D,E orders are safe at T0; after P1 gets (1,0,2), available=(2,3,0), while P3 needs C=1, so D,E cannot start. C remains safe. The further P0 request produces an unsafe state, not proof of actual deadlock. Whether C,D,E refer to before or after the first grant is a wording ambiguity. |
| m_70d4944003ddae3e | 103 交大《資料結構與演算法》Q9 | devin | Supported. Shortest SIMPLE path with negative cycles is NP-hard by negating positive longest-simple-path weights: (2)=2. Maximum independent set on interval graphs is interval scheduling by earliest finishing time: (9)=1. Either-sign cycle detection is polynomial (negate for positive cycles). Other classifications agree. |
| m_a9d0ef911f63d806 | 101 交大《數學》Q4 | official | Supported. E=R^2: arbitrary (x,y) has a=(x+y)/2, b=cuberoot((x-y)/2). Only A (degree exactly 3, excluding zero) is not a vector space. Official A,E retained. |
| m_abef756230f5aafc | 100 台大《計算機系統》Q3 | devin | Objection supported: locking cannot make timer expiry plus blocking write atomic. But the child's own select/poll-before-blocking-write remedy was incomplete: readiness does not guarantee the whole write finishes. Corrected to nonblocking partial writes, readiness waits and an absolute deadline; established the sigsetjmp checkpoint before arming the timer. |
| m_b368e0bb96b1cea9 | 103 交大《離散數學與線性代數》Q4 | devin | Supported. Independently checked rank 2, orthogonal basis pairs, P=A A+, A x=P b for the given least-squares family, and A+ b=(-14,-28,6,32)/51. Two pivot coefficients are not a full four-coordinate solution; residual length sqrt(3) is not the requested minimum-length solution vector. |
| m_b407d872827de632 | 103 交大《資料結構與演算法》Q12 | devin | Supported. Read arrows from actual figure (B->C, D->B), then BFS augmentations S-A-B-T by 2 and S-C-D-T by 3 give max flow/min-cut=5. All 12 listed positive residual arcs match. Unused A->C, B->C, D->B retain original directions. |
| m_c27a9f5a16cc1d8f | 102 交大《資料結構與演算法》Q7 | drive | Invalid-rotation objection supported, but unqualified part (3) needed fixing. Diagram and simulation give parent(4)=7, parent(7)=2 after first three rotations. Additional left(1), left(6), right(3) have no required child. Inorder 1..7 assumes invalid rotations are no-ops; the literal seven-rotation sequence is undefined. Added [?]; drive marker retained. |
| m_c2df8b8a70db8d22 | 101 交大《計算機組織》Q9 | official | Supported for the actual signal wires in the figure, not the ID-stage control bundle. Cycle 5: EX lw3 gives ALUSrc=1,RegDst=0; MEM sw2 gives MemWrite=1; WB add1 gives MemToReg=0. Hence B,D, not B,C,D. Official letters retained. |
| m_cc144c0cf2fac857 | 100 交大《資料結構與演算法》Q54 | official | Blanket objection NOT sustained. Real-threshold gap reasoning is right, but Problem I explicitly requires INTEGER B. Example n=3,e=1 makes proposed B=4.5 illegal, so D is not a generally valid definition for arbitrary positive e. B=n is legal and suffices. Replaced objection and removed [?]; official D unchanged. If e were restricted so this B were integral, the question would again be ambiguous. |
| m_cec03837d66daa73 | 102 交大《計算機系統》Q19 | official | Suspicion supported under separate hierarchical CLA units, but retain [?]. p/g ready at 2; group G at 5; top-level c6 at 8; local c8 at 11; final XOR gives s8 at 13. Official 12 requires a different factoring/fan-in/timing convention not specified. A,B,C agree; D is false because c6 uses top-level carry. |
| m_d1fba798b2ed721c | 104 交大《離散數學與線性代數》Q5 | devin | Supported. range(L) is always a subset of R^m. Always false F,G,I,N; always true H,M; col(A)=R^m iff rank(A)=m, so only J in (c). kernel(L)=R^n implies L=0. |
| m_e3c656b3e76bbe2d | 100 交大《資料結構與演算法》Q37 | official | Supported. Floyd-Warshall handles negative edges (B false) and detects negative cycles through negative diagonal d_ii after relaxation (D false too). Official single answer B is incomplete. |
| m_e4088cfa4773bb83 | 101 交大《資料結構與演算法》Q57 | official | Supported on printed 'each vertex visited exactly once': Problem II is Hamiltonian path with a length cap, not ordinary shortest path. Floyd-Warshall does not solve it, so A is false too. Negating weights cannot make Bellman-Ford solve longest simple paths, so D is false. Official D retained. |
| m_fce786d5c3bca17b | 101 交大《計算機組織》Q10 | official | Supported. Five-stage simulation with instruction-6 lw -> instruction-7 add load-use stall: cycle 10 has EX add7, MEM bubble, WB lw6. Actual signal wires give RegDst=1 and MemToReg=1, hence A,C. Omitting the stall explains official A; official letters retained. |
| m_fe8ed09661e06e49 | 100 交大《資料結構與演算法》Q15 | official | Supported literally. Reflexivity demands xRx; asymmetry forbids it on a nonempty domain. Thus E. D (>=) is reflexive, ANTIsymmetric, transitive, suggesting a missing 'anti' in the question. Official D retained. |

## (d) Fixed-seed numerical/computational spot checks

Seed **20261106**, Python random.Random. Manually screened text-only eligibility pool fixed first: concrete arithmetic, traces, heaps, recurrences, enumeration or matrix calculations; conceptual-only and figure-dependent questions excluded. Sort IDs then stratified random sample: **14 計系 + 13 資演 + 13 數學 = 40**. Not uniform across all Devin answers and not a statistical error-rate estimate. A broad digit-containing initial filter admitted conceptual answers and was discarded before recomputation; reproducible final pools/sample: ~/keys-raw/review_sample.py and review-sample.json.

Pool sizes: {'計系': 37, '資演': 22, '數學': 42}. All selected files have src: devin.

Independent Python implementation: ~/keys-raw/recompute_answers.py; results: ~/keys-raw/recomputed.json. Integer/Fraction arithmetic where exact; NumPy floating point for matrix and radical checks, with integer/residual cross-checks. Recurrences tested across multiple n. Proof/asymptotic parts additionally assessed analytically. Scope is computational components, not formal verification of every proof sentence.

**Results: 38 match existing numerical answers (some already conditional); 1 numerical correction/qualification (RR utilization), and 1 newly underdetermined subanswer (segmentation).** No other sampled numerical errors found.

### Suspected errors and corrected values

- e9fe4a8835: old 15/16.1 ≈ 93.2% is a full-round approximation, not steady-state FIFO RR with concurrent independent I/O. Simulation starts I/O tasks at 0,1.1,...,9.9 ms; CPU task runs 11–16 ms. Only five I/O tasks are ahead of it in the ready queue when requeued. Steady state alternates five I/O bursts with a CPU quantum: 10/10.6=50/53≈94.34%. A repeated full period starts at 16.1 and 37.3 ms, with 20 ms work / 21.2 ms elapsed. Added [?] because I/O concurrency is unspecified and the common round model gives the old approximation; not claimed universal across I/O device models.
- c8a0b207cf (d): 'maximum four segments' does not follow from a MAXIMUM segment size of 1 GiB. Four full-sized segments cover 4 GiB VA; smaller segments allow more. Need minimum granularity / selector bits. Added [?]; a–c unchanged.

| Group | ID | Year / school / paper / question | Independent result | Assessment |
|---|---|---|---|---|
| 計系 | 144e766d3e | 101 台大《計算機系統》Q2 | (2020000, 8040000, 12) | a,b,d match; c's 5 blocks assumes one data block per traversed directory (already flagged). |
| 計系 | 1843cb536f | 103 台大《計算機結構與作業系統》Q7 | (Fraction(5, 2), Fraction(10, 3), Fraction(10, 7), Fraction(20, 13)) | Matches existing answer. |
| 計系 | 3a18d18414 | 104 清大《計算機系統》Q13 | (16, Fraction(89, 19), Fraction(89, 29)) | Matches conditional 8-bank / 4-bank answers; bank count is genuinely unspecified. |
| 計系 | 6c5a684dfb | 102 清大《計算機系統》Q7 | (1050, 400, 2000, 250) | Matches existing answer. |
| 計系 | 0e9338a0cb | 102 清大《計算機系統》Q1 | ([190, 120, 80, 10, 280, 900, 910], [280, 900, 910, 190, 120, 80, 10], [280, 900, 910, 10, 80, 120, 190]) | Matches existing answer. |
| 計系 | 918506b0b2 | 106 清大《計算機系統》Q9 | 3072000 | Matches existing answer. |
| 計系 | 55d2bf6cba | 102 台大《計算機系統》Q12 | (Fraction(1, 8), Fraction(1, 8)) | Streaming: 128 distinct lines/1024 references; no victim reuse; ideal timely stream buffer has one initial miss. |
| 計系 | f12cfb95ad | 102 清大《計算機系統》Q13 | (Fraction(49, 50), Fraction(24, 25)) | Matches existing answer. |
| 計系 | da230524eb | 107 清大《計算機系統》Q9 | (8, 10) | Matches existing answer. |
| 計系 | 961d11d272 | 102 清大《計算機系統》Q9 | (9, 12) | Matches existing answer. |
| 計系 | e9fe4a8835 | 107 清大《計算機系統》Q1 | 50/53 | Corrected/qualified: FIFO RR with independent concurrent I/O settles at 20/21.2=50/53=94.34%; 15/16.1 assumes all ten I/O tasks run between CPU slices, contradicted by wake-up queue. |
| 計系 | e5645b7461 | 106 清大《計算機系統》Q8 | -13 | Matches existing answer. |
| 計系 | c8a0b207cf | 101 清大《計算機系統》Q3 | (268435456, 16777216, Fraction(335, 1)) | a-c match. d is not determined: 4 maximum-sized segments cover 4 GiB, but smaller segments allow more than 4; marked [?]. |
| 計系 | fe99030a42 | 106 台大《計算機系統》Q1 | (Fraction(3600, 1), Fraction(3625, 1)) | Matches existing answer. |
| 資演 | 82d7ccda5d | 105 台大《資料結構與演算法》Q7 | 7 | Matches existing answer. |
| 資演 | bae27ae502 | 100 清大《基礎計算機科學》Q3 | [1, 2, 3, 2, 1, 2, 1, 0] | Matches existing answer. |
| 資演 | 69c4fd2cfd | 104 清大《基礎計算機科學》Q11 | 5 | Matches existing objection: 4 comparisons cannot distinguish 24 permutations (16 leaves). |
| 資演 | 808ab138af | 104 清大《基礎計算機科學》Q6 | ([5, 15, 9, 34, 30, 28], [28, 30, 34], [5, 9, 15]) | Heap and popped keys match; BST inserts 5,9,15,45,3,12, matching answer. |
| 資演 | d0b4b89fc9 | 101 清大《基礎計算機科學》Q7 | (True, [1, 1, 3, 21]) | Catalan counts through n=8; exact-height counts 1,1,3,21 agree with independent at-most-height recurrence. |
| 資演 | m_dd69738bba6ce3bc | 106 台大《資料結構與演算法》Q2 | (True, False, True) | Matches existing answer. |
| 資演 | f6b69f2d1a | 102 清大《基礎計算機科學》Q6 | ([[3, 0, 0], [1, 4, 0], [-1, 1, 5]], 5, 30) | Matches existing answer. |
| 資演 | m_402625b294ecec77 | 106 交大《資料結構與演算法》Q3 | [3, 2, 7, 8] | Matches existing answer. |
| 資演 | m_4c177d9376b5a4fb | 106 交大《資料結構與演算法》Q4 | [6, 8, 10, 9, 18, 15] | Matches existing answer. |
| 資演 | 35fbefc6e8 | 106 清大《基礎計算機科學》Q1 | [5, 7, 10, 15, 29, 28, 19, 34, 60] | Matches existing answer. |
| 資演 | 469341e6ff | 100 清大《基礎計算機科學》Q5 | [20, 31, 43, 57, 100] | Matches existing answer. |
| 資演 | m_e8bbdff9febdd685 | 103 台大《資料結構與演算法》Q2 | ([1, 8, 28, 56, 70, 56, 28, 8, 1], 256) | Matches existing answer. |
| 資演 | m_00af7882d4ee9b5d | 106 交大《資料結構與演算法》Q2 | 6 | Numeric prefix evaluates to 6; independent infix parse gives Add(A,Div(Mul(B,Sub(C,D)),E)), agreeing with prefix/postfix. |
| 數學 | 39464e78d3 | 104 清大《基礎計算機科學》Q4 | [1, 4, 13, 40, 121, 364, 1093, 3280, 9841, 29524] | Matches existing answer. |
| 數學 | m_d4eeae4dddc0a3cf | 105 交大《數學》Q3 | [[10, 3], [32, 10]] | Matches existing answer. |
| 數學 | m_6c33cea11f7e3c66 | 105 交大《數學》Q10 | (11, [28], [169, 311, 572]) | Matches existing answer. |
| 數學 | m_3db56a4736becf89 | 106 交大《數學》Q9 | ([4, -1, -2, 2], [0, 0, 0], 0, True) | Matches existing answer. |
| 數學 | m_8af62953c892a241 | 105 交大《數學》Q4 | (-20, [0, 0, 0]) | Matches existing answer. |
| 數學 | d09bfcbc88 | 106 台大《數學》Q4 | True | Matches existing answer. |
| 數學 | c38aadb69a | 105 台大《數學》Q14 | [2, 4, 16] | Count matches printed equal-complement definition (not standard self-dual terminology); negated self-dual definition coincidentally has same count. |
| 數學 | m_fc7897eb01e6ea74 | 105 交大《數學》Q5 | Exact 365-day Fraction iteration: CC=3+2^-364, YJ=3+2^-365 | Matches existing answer. |
| 數學 | dm03_f4df8f7fe1853aac | 107 交大《數學》Q7 | (Fraction(1, 64), Fraction(5, 16), Fraction(1, 2)) | Matches existing answer. |
| 數學 | m_1ae44a9a2735596f | 107 交大《數學》Q1 | 4 | Matches existing answer. |
| 數學 | m_36f7712c097bfe3b | 106 台大《數學》Q8 | 325 initial-condition/n checks: 25 pairs, n=0..12 | Matches 25 initial-condition pairs through n=12; characteristic roots satisfy r²-r-1=0. |
| 數學 | m_d58d38394e4ba156 | 107 交大《數學》Q2 | 72 | Matches existing answer. |
| 數學 | 351863faeb | 105 台大《數學》Q11 | n=0..20 recurrence agrees with 6*2^n-n-2 | Matches existing answer. |

## Changed answer files (uncommitted)

All under Practice Exams/_src/_a/. Exactly eight files. Four newly flagged files and one removed flag change total [?] count 55 → 58.

| File | Change |
|---|---|
| c8a0b207cf.md | Qualified segmentation (d): four maximal-sized segments suffice, but maximum count is underdetermined; added [?]. |
| e9fe4a8835.md | Corrected/qualified RR utilization to 50/53=94.34% for FIFO concurrent-I/O scheduling; retained 93.2% as a round approximation and added [?]. |
| m_04fbb0ca028a7ae3.md | Corrected full-tree leaf depths for 3/4; added [?] about unary nodes. |
| m_3464c2ceefafe40c.md | Softened categorical reversal of Drive; hardware assumptions are essential. |
| m_3e269d668e0fdd3e.md | Note distinguishes atomic-concatenation outcomes from actual undefined behavior; key untouched. |
| m_abef756230f5aafc.md | Corrected timeout remedy: checkpoint before alarm; nonblocking partial-write loop and absolute deadline. |
| m_c27a9f5a16cc1d8f.md | Qualified undefined rotation sequence; sorted inorder assumes invalid rotations are no-ops; added [?]. |
| m_cc144c0cf2fac857.md | Corrected disagreement note for integer B; removed unsupported [?]; key untouched. |

## Verification and limitations

After final answer edit:

    $ python3 'Practice Exams/_tools/lint_a.py' --all
    1053 checked, 0 errors
    $ git diff --check
    (no diagnostics; exit 0)

Independent computations:

    $ python3 ~/keys-raw/recompute_answers.py
    PASS: 40 fixed-seed numerical/computational answer checks; 1 newly flagged underdetermined subanswer (c8a0b207cf d).
    $ python3 ~/keys-raw/check_disagreements.py
    PASS: 13 numerical/diagram disagreement checks; all four needed diagrams read from existing question PDFs.

Review-harness development: sample simulation exposed the RR discrepancy, then a sign typo in the expected determinant (-20, not +20); corrected expectations/model and all 40 checks completed. Disagreement simulation initially omitted instruction-7's hold in ID; corrected EX-onward timing, with no change in verdict.

No question transcriptions, key index, shared tools, configuration or PDFs changed. No PDF regeneration or check.py run: answer text validated by answer lint and independent computation. Changed answers are visually unverified in regenerated answer PDFs. Diagram evidence: ~/keys-raw/figure-review-{0,1,2,3}.png.

Remaining scope: non-sampled/non-annotated answers, including new batches beyond counts/uncertainty census, were not independently solved. Flagged proof/program sketches remain listed as incomplete, not claimed fully proved.
