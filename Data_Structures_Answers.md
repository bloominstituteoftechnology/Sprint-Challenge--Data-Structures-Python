Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
 - O(n) since it has to go through each of the items

2. What is the space complexity of your `depth_first_for_each` function?
 - O(1) because no new variables or constants are being created. Unless python creates a new variable when one is passed into a function, then it would be O(n) since I use recursion, but I don't believe that happens.

3. What is the runtime complexity of your `breadth_first_for_each` method?
 - O(n) since it has to go through each of the items

4. What is the space complexity of your `breadth_first_for_each` method?
 - O(n) since all but the first node are being added to a deque


** n: first set of names, k: second set of names **

5. What is the runtime complexity of the provided code in `names.py`?
 - O(n*k) because of the nested for loop. This turns out to O(n^2) since both lists are the same size

6. What is the space complexity of the provided code in `names.py`?
 - O(n) since the names in the files weren't stored anywhere other than the initial lists composed when the files were read 

7. What is the runtime complexity of your optimized code in `names.py`?
 - O(n) where n is the largest and k is the smallest, because I turn both into sets which is O(n + k) and then look at the intersection which is O(k)

8. What is the space complexity of your optimized code in `names.py`?
 - O(n + k) plus a little extra because I create a set for each of the names lists.
