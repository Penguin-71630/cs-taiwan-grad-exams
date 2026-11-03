請遵守下列規定回答以下問題，違者該題不計分。

- 不要書寫任何程式碼或代碼。請以文字，圖表，數學符號陳述你要表達的概念。
- 一個問題包括兩個子題。一個子題的回答以一頁為限，並請按順序寫在完整的一頁。請先想好再動筆。如果字寫太小或是太潦草或是英文文法問題導致閱卷者無法理解你的想法，該題不計分。
- 一個問題包括兩個子題。前一個子題是觀念的陳述，佔 10 分，後一個子題是觀念的證明，佔 15 分。證明部分有倒扣，答對得 15 分，答錯倒扣 10 分，不答得 0 分。知之為知之，不知為不知，是知也。瞎掰不能解決問題，珍惜分數，遠離倒扣。

4\. (25 points) We are given a network of $C$ cities and $R$ roads. All roads are one-way, i.e., if a road goes from city $u$ to city $v$ then there will be no roads going from $v$ to $u$. In addition, the roads will not form any *cycle*. That is, you cannot start from a city $v$, go through several cities, and go back to $v$. Finally we assume that there is a capital that can go to all other cities in the network.

We want to compute the *minimum* number of days for a tourist to go from the capital to each non-capital city. When a tourist encounters a city $v$, he will spend $c(v)>0$ days to visit all attractions in $v$. When a tourist goes from city $u$ to city $v$, he will spend $r(u,v)>0$ days on the road. Now given the $c$ function values for all cities, and $r$ function values for all roads, please compute the *minimum* number of days for a tourist to go from the capital to each non-capital city. We use $M(v)$ to denote this minimum number of days from the capital to a city $v$.

We illustrate the problem with an example of four cities $A$, $B$, $C$, $D$ and four roads. Let $A$ be the capital and $c(A)=c(B)=c(C)=c(D)=1$, and $r(A,B)=r(A,C)=r(B,D)=2$, and $r(C,D)=10$. Then $M(D)=c(A)+r(A,B)+c(B)+r(B,D)+c(D)=7$. Similarly $M(B)=M(C)=4$.

(a) (10 points) Please derive an *optimal* algorithm to compute the $M$ function for all cities other than the capital.\
(b) (15 points) Please analyze the time complexity of your algorithm and prove that it is optimal.
