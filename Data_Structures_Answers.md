Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
   
   Runtime is O(n) since every node is traversed

2. What is the space complexity of your `depth_first_for_each` function?

   <!-- Space complexity is O(1). There is no stack taking up space it  -->
   Implicit stack would be O(log n) the length of the tree.
   But worse case is O(n) since it could be a completely imbalanced tree.

3. What is the runtime complexity of your `breadth_first_for_each` method?

   Runtime is O(n) since every node is traversed

4. What is the space complexity of your `breadth_first_for_each` method?

   Space complexity is O(n/2 + 1) => O(n) The size of the queue was less than the size of the data.

   <!-- Space complexity is O(log n). The size of the queue was less than the size of the data. -->


5. What is the runtime complexity of the provided code in `names.py`?

   Runtime is O(n^2) since it was a nested for loop.

6. What is the space complexity of the provided code in `names.py`?

  Space complexity is O(n). In the worse case, all names would be duplicates and would have to be added to the duplicates array.

7. What is the runtime complexity of your optimized code in `names.py`?

  Runtime is O(n) since each name was checked. But they were done in separate for loops.

8. What is the space complexity of your optimized code in `names.py`?

  Space complexity is O(n). In the worse case, all names would be duplicates and would have to be added to the duplicates array. And a frequency dict of all the names. But O(2n) => O(n)
