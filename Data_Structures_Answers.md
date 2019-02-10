Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

2. What is the space complexity of your `depth_first_for_each` function?

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

The runtime complexity of the optimized code is O(n) due to the use of a hash table. Since the only operation being used is a simple check to see whether a particular name is at a particular index, the growth is linear. We do not have to adjust our runtime based on the size of the single_names set since the only relevant number is the input size. Input size alone will always determine the number of iterations and therefore the runtime.

8. What is the space complexity of your optimized code in `names.py`?

The space complexity is also O(n), again because we're simply storing values that are related to the number of inputs. This is why hash tables are not necessarily the most space-efficient solution, but since our concern here was runtime it is a highly effective solution.