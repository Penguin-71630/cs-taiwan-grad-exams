3\. (17 points) Huffman coding is a type of coding schemes used for lossless data compression. In the coding scheme, each character in a file is represented by a unique string, which is called a codeword. The length of a codeword that represents a frequently appeared character in the input file is usually shorter than other codewords as well as the original character. Thus, when the entire file is encoded by converting all characters in the file to codewords which represent them, the total length can usually be significantly reduced. In a binary Huffman code, the number of symbols that can be used to form a codeword is 2. We can also use a $n$-ary Huffman code, in which the number of symbols that can be used to form a codeword is $n$.

(a) (8 points) Please prove that the decoding tree which represents an optimal code for a file (using which the encoded file has a minimum length) must be a full $n$-ary tree, i.e., all non-leaf nodes in the tree have $n$ children.

(b) (4 points) You are given the numbers of appearances of all characters in a file as follows: {'*a*' : 700, '*b*' : 400, '*c*' : 200, '*d*' : 100, '*e*' : 1300, '*f*' : 2400, '*g*' : 100}. What are the lengths of the codewords for the characters 'a' and 'c', respectively, in a 3-ary Huffman code derived for this file?

(c) (5 points) Which of the following statements are correct? Please mark all correct statements.

i. A Huffman code is a fixed-length code.\
ii. A Huffman code is a prefix code.\
iii. If a file contains a sequence of 8-bit characters such that the maximum character frequency is less than **three times** of the minimum character frequency, then binary Huffman codings always cannot do better than an ordinary 8-bit fixed-length code.\
iv. If a file contains a sequence of 8-bit characters such that the maximum character frequency is less than **twice** of the minimum character frequency, then binary Huffman codings always cannot do better than an ordinary 8-bit fixed-length code.\
v. If a file contains a sequence of 8-bit characters such that the maximum character frequency is less than **1.5 times** of the minimum character frequency, then binary Huffman codings always cannot do better than an ordinary 8-bit fixed-length code.
