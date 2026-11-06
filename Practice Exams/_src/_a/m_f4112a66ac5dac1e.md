<!-- src: devin -->
Scan once: push operators on a stack, operand strings in queues; on each `)` pop operator and its two operands and enqueue `op + left + right` as one prefix sub-expression; the last remaining one is the answer. [?] 程式題，僅給演算法要點
