<!-- src: drive -->
Add 8 2-to-1 MUXes (select = Mode) before and after the left-shifter: when Mode=1, reverse the bits of the input ($X_i = X'_{7-i}$) and reverse the output ($Y'_i = Y_{7-i}$); when Mode=0, pass straight through; $C = C'$
