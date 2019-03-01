Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    O(N). Every node will be accessed.
2. What is the space complexity of your `depth_first_for_each` function?
    If the space taken up by the array in the callback is taken into account, O(N). Otherwise, O(1).
3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?
    O(N squared). We compare N items to N items in an inner loop.
6. What is the space complexity of the provided code in `names.py`?
    O(N), the space taken up depends on the size of N (the files given). Would the duplicates array be considered a constant that would be dropped?
7. What is the runtime complexity of your optimized code in `names.py`?
    O(N)
8. What is the space complexity of your optimized code in `names.py`?
    Greater than O(N) since I create two new dictionaries of N size. Maybe O(n log n)?