Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1), since the number of operations doesn't change with the length of the list.

2. What is the space complexity of your ring buffer's `append` function?

O(1), since the amount of space used doesn't change with the use of the `append` function.

3. What is the runtime complexity of your ring buffer's `get` method?

O(n), since the number of operations increases with the amount of items in storage.

4. What is the space complexity of your ring buffer's `get` method?

O(n), since the amount of memory needed in the created list increases with the amount of non-null items in storage. 

5. What is the runtime complexity of the provided code in `names.py`?

This code has a runtime complexity of O(n^2).

6. What is the space complexity of the provided code in `names.py`?

This code has a space complexity of O(n).

7. What is the runtime complexity of your optimized code in `names.py`?

<!-- My code has a runtime complexity of O(n log n), since I go through n searches, and each search takes a log n number of operations in the binary search tree. -->

My code has a runtime complexity of O(2n), which simplifies to O(n).

8. What is the space complexity of your optimized code in `names.py`?

My code has a space complexity of O(n).