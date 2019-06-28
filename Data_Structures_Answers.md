Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

Constant time O(1) because I am using subscripting to override the existing element at the given index.

2. What is the space complexity of your ring buffer's `append` function?

The space complexity is also O(1) because the number of variables never changes.

3. What is the runtime complexity of your ring buffer's `get` method?

The `get` method is linear time O(n), because the number of operations is directly related to n.

4. What is the space complexity of your ring buffer's `get` method?

The `get` space complexity is also O(n) because space is required for filtered_list and requires n elements to appended.

5. What is the runtime complexity of the provided code in `names.py`?

The runtime of the original code was quadratic O(n^2) because it required nested looping to find the duplicate elements.

6. What is the space complexity of the provided code in `names.py`?

The space complexity was O(n) because the size of duplicates was directly connected to n.

7. What is the runtime complexity of your optimized code in `names.py`?

O(n log n) is the runtime of the code I used in names.py. This is the case because I used ran binary search tree methods according to n. 

8. What is the space complexity of your optimized code in `names.py`?

O(n) is the space complexity of my optimized code because both the tree and duplicates grow in correlation to n.
