Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
O(n) since it has to go through each node in the tree

2. What is the space complexity of your `depth_first_for_each` function?
O(h) where h is the height of the tree, this is because the addresses are removed from the stack when returning and this old stack frame is reused when making a new call from the level above.

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?
It is O (n * k) where n is the number of inputs for names1 and k is the number of inputs for names2 in this particular example they both have equal amounts of inputs so it comes out to o (n ** 2)

6. What is the space complexity of the provided code in `names.py`?
The space complexity is O(n) where n is the length of the longer list, since it has to store those values in a list after it reads them from the file.

7. What is the runtime complexity of your optimized code in `names.py`?
I was able to make my code run in under one hundreth of a second on my device, it ran in 0.003 seconds. I achieved this using sets and then checking for where they intersect. This comes out to O(n) where n is the length of the shorter list, this is because It has to iterate through the shorter list and then it looks it up in the other set which is o(1) lookup in a set.


8. What is the space complexity of your optimized code in `names.py`?
The space complexity is O(n) where n is the length of the longer list, since it has to store those values in a list after it reads them from the file.