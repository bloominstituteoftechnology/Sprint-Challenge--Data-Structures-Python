Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1) Constant

2. What is the space complexity of your ring buffer's `append` function?
Constant. No new variables are created. Therefore no new memory is allocated.

3. What is the runtime complexity of your ring buffer's `get` method?
O(n) Linear

4. What is the space complexity of your ring buffer's `get` method?
O(2) constant. Two variables are created. One is to store the returned values. The second is to run through the for loop.

5. What is the runtime complexity of the provided code in `names.py`?
O(names_1 * names_2), Could also be O(n^2) because both lists are the same size.

6. What is the space complexity of the provided code in `names.py`?
O(2) Constant. There are two variables created. One for the for loop and one to store the duplicate names.

7. What is the runtime complexity of your optimized code in `names.py`?
O(n) Linear

8. What is the space complexity of your optimized code in `names.py`?
O(2) Constant. There are two variables created. One for the for loop and one to store the duplicate names.