<!-- src: devin -->
A. Static: always not-taken / backward-taken-forward-not-taken (BTFN); dynamic: 1-bit or 2-bit saturating-counter BHT (also gshare/tournament)\
B. Procedure returns, indirect calls via function pointers / virtual functions (C++ virtual methods), switch-case jump tables, dynamic linking (PLT) and interpreters; procedure return is most frequent\
C. The target address comes from a register and can differ on each execution (many targets), so predicting taken/not-taken is not enough; a BTB holds only one last target per branch
