Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
 - O(n) since it has to go through each of the items

2. What is the space complexity of your `depth_first_for_each` function?
 - O(1) because no new variables or constants are being created. Unless python creates a new variable when one is passed into a function, then it would be O(n) since I use recursion, but I don't believe that happens.

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?
 - O(n^2) because of the nested for loop

6. What is the space complexity of the provided code in `names.py`?
 - O(1) since the names in the files weren't stored anywhere outside of themselves (O(duplicates) with the constant)

7. What is the runtime complexity of your optimized code in `names.py`?
 - O(n) (O(2n) with the constant)

8. What is the space complexity of your optimized code in `names.py`?
 - O(n) since I create a dictionary with each of the 1000 names in names_1 (O(n/2 + duplicates) with constants)
