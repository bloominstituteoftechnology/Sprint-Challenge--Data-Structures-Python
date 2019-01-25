Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    O(n). Each node is visited once.

2. What is the space complexity of your `depth_first_for_each` function?
    O(b^m).  b is the maximum branching factor of the search tree and m is the maximum depth of the state space.

3. What is the runtime complexity of your `breadth_first_for_each` method?
    pass
4. What is the space complexity of your `breadth_first_for_each` method?
    pass

5. What is the runtime complexity of the provided code in `names.py`?
    O(n * n). There are two 'for' loops.

6. What is the space complexity of the provided code in `names.py`?
    O(n). The algorithm will store names_1, names_2, the duplicates array and the current names to compare.

7. What is the runtime complexity of your optimized code in `names.py`?
    O(1) for 'set' call because it uses a hash table implementation. O(n) for intersection.  Overall, O(n).

8. What is the space complexity of your optimized code in `names.py`?
    O(n) for 'set' because it is a hash table implementation. O(n) for duplicates.  Overall, O(n).
