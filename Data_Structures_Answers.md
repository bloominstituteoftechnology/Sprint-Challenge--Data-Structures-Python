Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    O(n) because we call the method once per node and there are n nodes
2. What is the space complexity of your `depth_first_for_each` function?
    O(1) because we don't allocate any space for a new data structure
3. What is the runtime complexity of your `breadth_first_for_each` method?
    O(n)
4. What is the space complexity of your `breadth_first_for_each` method?
    O(n)

5. What is the runtime complexity of the provided code in `names.py`?
    O(n^2) because there is a nested loop insdie a loop and each loop is O(n)
6. What is the space complexity of the provided code in `names.py`?
    O(n) because we create new list that depends on the number of duplicate names found
7. What is the runtime complexity of your optimized code in `names.py`?
    O(n) because we iterrate through only one set of names at least once
8. What is the space complexity of your optimized code in `names.py`?
    O(n) because I used a set() which makes it O(n), and if there are duplicates then it would be O(n) + O(n) => O(2 * n) => O(n)