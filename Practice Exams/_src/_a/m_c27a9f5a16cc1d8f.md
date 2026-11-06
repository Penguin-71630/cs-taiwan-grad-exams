<!-- src: drive -->
(1) 7\
(2) 2\
(3) [?] The seven-rotation sequence is not defined: left_rotate(1) has no right child. If invalid rotations are treated as no-ops, the inorder sequence is 1 2 3 4 5 6 7.
> 註：後四次旋轉中 left_rotate(1)、left_rotate(6)、right_rotate(3) 無對應子節點而無法執行；若將非法旋轉視為不動作，合法旋轉不改變中序，才可得 (3) 的序列。
