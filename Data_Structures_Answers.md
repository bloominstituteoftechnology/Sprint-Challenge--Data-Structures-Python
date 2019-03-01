Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
  O(n) Because we need to run through every item in the tree once.

2. What is the space complexity of your `depth_first_for_each` function?
  O(n), I believe, because you hypothetically could need to store 
  every node in the stack, depending on the balance and because it is
  dependent on the length of the longest branch.

3. What is the runtime complexity of your `breadth_first_for_each` method?
  O(n)

4. What is the space complexity of your `breadth_first_for_each` method?
  O(n)


5. What is the runtime complexity of the provided code in `names.py`?
  O(n^2) Because we have to run through a second loop for every time we
  run through an intitial loop that must be run through for every item
  in the input array.

6. What is the space complexity of the provided code in `names.py`?
  O(n) Because the space required grows linearly with the inputs.

7. What is the runtime complexity of your optimized code in `names.py`?
  O(n) Because the number of iterations of any given loop depends only on
  the size of the input, and not on the number of loops of a parent loop.

8. What is the space complexity of your optimized code in `names.py`?
  O(n) 