1\. (30 points) *In this problem, and this problem only,* please choose among the following items and show your answers by the item labels.

| [A] $O(1)$ | [B] $O(n)$ | [C] $O(\log n)$ | [D] $O(n\log n)$ |
|:---|:---|:---|:---|

The `vector` data structure is basically a flexible-size array, i.e., the number of elements inside the `vector` can be unlimited. The `vector` data structure can be implemented with either the usual fixed-length `array` or a singly `linked list`.

The `vector` can be implemented by a fixed-length `array` with an auxiliary `length` information *without* wasting any other space of the array. Then, accessing an element within the vector by index is trivial. But in the worst case, when an element is inserted into the vector, a new array needs to be created and all the contents in the original array need to be moved; similarly, when an element is removed from the vector, the creating and moving steps need to be performed, too.

The `vector` can also be implemented by a singly `linked list` *without* wasting any other space. Then, inserting an element into or removing an element from the vector by index does not need moving any contents.

Assume there are $n$ elements in a `vector` $V$, what is the asymptotic worst-case running time for each operation under different implementations?

| | `array` | `linked list` |
|:---:|:---:|:---:|
| $Access(V,i)$ | (1) | (2) |
| $Insert(V,x,i)$ | (3) | (4) |
| $Delete(V,i)$ | (5) | (6) |

Here $Access(V,i)$ returns the element at the $i$-th position in $V$, $Insert(V,x,i)$ inserts an element $x$ into the $i$-th position in $V$, and $Delete(V,i)$ deletes an element at the $i$-th position in $V$. Both $Insert$ and $Delete$ will change the size of $V$.

Besides the useful `singly linked list`, `doubly linked list` is a more continent data structure, since a node can have two links point to both its successor and predecessor. Consider a list $L$ that consists of $n$ objects with one root pointer and one tail pointer pointing to its first and last object. What is the asymptotic worst-case running time for each dynamic-set operation listed in the following table?

| | `singly linked list` | `doubly linked list` |
|:---:|:---:|:---:|
| $Search(L,k)$ | (7) | (8) |
| $Remove(L,p)$ | (9) | (10) |

Here $Search(L,k)$ returns the object whose key equals $k$ in $L$, and $Remove(L,x)$ removes a node pointed by pointer $p$ from $L$.
