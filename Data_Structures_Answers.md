Add your answers to the questions below.

`cb(self.value)` is O(1) since it only takes the passed in values and append it to an array.

1. What is the runtime complexity of your `depth_first_for_each` method?

   - O(log n) because I used recursion to traverse on each branches of the tree and the height of the tree is based on log n.

2. What is the space complexity of your `depth_first_for_each` function?

   - O(log n)

3. What is the runtime complexity of your `breadth_first_for_each` method?

   - O(n) because bfs touches every node just once.

4. What is the space complexity of your `breadth_first_for_each` method?
   - O(n) because every time each node that is being appended in the array grows in linear time.

5) What is the runtime complexity of the provided code in `names.py`?

   - O(n^2) because there are nested for loops and each for loop has a runtime complexity of O(n). It took 7.971049785614014 seconds to run it in my terminal.

6) What is the space complexity of the provided code in `names.py`?

   - O(2n) => O(n) since we're comparing two lists

7) What is the runtime complexity of your optimized code in `names.py`?

   - O(n) because even though sets are O(1) in python, lists are O(n) in average runtime. It took 0.006497859954833984 seconds to run it in my terminal.

8) What is the space complexity of your optimized code in `names.py`?
   - O(n) since we store the duplicated names in a list
