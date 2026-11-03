7\. (18 points) A *palindrome* is a string that reads the same from the left and from the right. For example, REDDER, I, ROTATOR, MOM, are palindromes. From a non-palindrome string, you can always remove an arbitrary number of characters from it to make it a palindrome. For example, from both ADAM and ADMA, you can remove 'M' to obtain a palindrome, ADA. In both cases, we say that ADA is the longest palindrome subsequence in the original strings, ADAM and ADMA.

We would like to derive a dynamic programming algorithm to determine the length of the longest palindrome subsequence in a string. You are given the string $S$ of length $n$ in the form of a character array $S=s[]$, where $s[i]$ is the $i$-th character in the string, $1\le i\le n$.

(a) (12 points) As the first step, please complete the following equation to represent the length of the longest palindrome subsequence in the given string $S$ by filling out the blanks. $L(i,j)$ represents the length of the longest palindrome subsequence in $s[i..j]$, a substring of $S$ that starts from the $i$-th character and ends at the $j$-th character of $S$.\
$L(i,j)$ is defined for $1\le i\le n, 1\le j\le n, j\ge i-1$, and

$$L(i,j)=\begin{cases} \underline{\qquad(1)\qquad} & ,\text{if } i=j+1 \\ \underline{\qquad(2)\qquad} & ,\text{if } i=j \\ \underline{\qquad(3)\qquad} & ,\text{if } i<j \text{ and } s[i]==s[j] \\ \underline{\qquad(4)\qquad} & ,\text{otherwise.} \end{cases}$$

(b) (6 points) Calculate the length of the longest palindrome sequence in the string CABDAACBADFA.
