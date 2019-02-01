Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    O(N+E) where n is nodes and e is edges but this is only if we store the tree as an array

2. What is the space complexity of your `depth_first_for_each` function?
    I think it would depend on the implementation and since I did BFS im not sure. Recursive would have to be
    the depth of the recursion stack. Iteratively It would be all the nodes in the tree. O(N)

3. What is the runtime complexity of your `breadth_first_for_each` method?
    O(N+E) where n is nodes and e is edges. This because we go over every node and each edge of it is travelled once down and once up.

4. What is the space complexity of your `breadth_first_for_each` method?
    There are two arrays in the search one is the queue and the other is the visited nodes. Worst case they would have to hold all the nodes making the space complexity O(N)

5. What is the runtime complexity of the provided code in `names.py`?
    It was O(4n) since it looped over all the names 4 times.

6. What is the space complexity of the provided code in `names.py`?
    It was O(2n) since the code stored 2 copies of the names in the files as lists.

7. What is the runtime complexity of your optimized code in `names.py`?
    The actual runtime was  0.005314826965332031 seconds. But this is actually O(2n/log(n))

8. What is the space complexity of your optimized code in `names.py`?
    Space complexity is O(4n) as the code used the two existing lists and also created 2 sets of the data.
