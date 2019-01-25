## Sprint Challenge: Data Structures

In this week's Sprint you implemented some classic and fundamental data structures and learned about how to go about evaluating their respective runtimes and performance. This Sprint Challenge aims to assess your comfort with these topics through exercises that build on the data structures you implemented and the algorithmic intuition you've started to build up.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your Challenge score is a measure of your ability to work independently using the material covered throughout this sprint. You need to demonstrate proficiency in the concepts and objectives that were introduced and that you practiced in the preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your submitted work reflects your proficiency in the concepts and topics that were covered this week.

You have three hours to complete this Sprint Challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons) and it also helps your project manager to more thoroughly assess your work.

## Description

This Sprint Challenge is split into three parts:

1. Writing an algorithm to traverse through a binary search tree
2. Optimizing some inefficient code
3. Analyzing time and space complexities from parts 1 and 2

### Minimum Viable Product


#### Task 1. Implement Depth-First or Breadth-First Traversal on the Binary Search Tree Class 

Navigate into the `search` directory. Inside, you'll see the `binary-search-tree.py` file with a complete implementation of the binary search tree class. Your first task is to implement either `depth_first_for_each` or `breadth_first_for_each` on the `BinarySearchTree` class:

   * `depth_first_for_each(cb)` receives an anonymous function as a parameter. It should then execute the anonymous function on each node in the tree in [depth-first](https://en.wikipedia.org/wiki/Depth-first_search) order. Your task is to implement the logic to traverse the tree in depth-first in-order fashion (as opposed to pre-order or post-order). Note that the pseudocode showcased on the Wikipedia article traverses the tree in-order. 

   * Remember that the anonymous function is supplied by the caller of the method. All you have to do is ensure that the anonymous function is being called on each tree node in the desired order.
   
     _HINT_: In order to achieve depth-first order, you'll probably want to utilize a Stack data structure. 

     * Run `python test_depth_first_search.py` to test your depth-first search implementation.

   * `breadth_first_for_each(cb)` receives a callback function as a parameter. It should then execute the anonymous function on each node in the tree in [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) order. Your task is to implement the logic to traverse the tree in left-to-right breadth-first fashion.
   
   * Remember that the anonymous function is supplied by the caller of the method. All you have to do is ensure that the anonymous function is being called on each tree node in the desired order.
   
     _HINT_: In order to achieve breadth-first order, you'll probably want to utilize a Queue data structure.

     * Run `python test_breadth_first_search.py` to test your breadth-first search implementation.

> Note that in Python, anonymous functions are referred to as "lambda functions". When passing in an anonymous function as input to either `depth_first_for_each` or `breadth_first_for_each`, you'll want to define them as lambda functions. For more information on lambda functions, check out this documentation: [https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

> Note that it is not your job to worry about what the callback function being passed in is doing. That is up to the user of your traversal method. All you care about when implementing the traversal method is to call the passed-in callback in either depth-first or breadth-first order, depending on which traversal method you're implementing. 


#### Task 2. Runtime Optimization

Navigate into the `names` directory. Here you will find two text files containing 10,000 names each, along with a program `names.py` that compares the two files and prints out duplicate name entries. Try running the code with `python3 names.py`. Be patient because it might take a while: approximately six seconds on my laptop. What is the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the code. Can you get the runtime to under a second? Under one hundredth of a second?

(Hint: You might try importing a data structure you built during the week)

#### Task 3. Analyze some runtimes

Open up the `Data_Structures_Answers.md` file. This is where you'll jot down your answers for the runtimes of the functions you just implemented. If you implemented depth-first traversal, just answer the questions pertaining to the depth-first traversal algorithm. If you implemented breadth-first traversal, just answer the questions pertaining to breadth-first traversal. 

Also, include the runtime and space complexities of the original code and your optimized solution from `names.py`.

### Stretch Problems

1. Implement the other tree traversal algorithm that you didn't implement on the `BinarySearchTree` class. Run the appropriate test file to test your implementation's correctness. Then go back to the `Data_Structures_Answers.md` file and answer the time and space complexity questions pertaining to the traveral method you just implemented.

2. Say your code from `names.py` is to run on an embedded computer with very limited RAM. Because of this, memory is extremely constrained and you are only allowed to store names in arrays (i.e. Python lists). How would you go about optimizing the code under these conditions? Try it out and compare your solution to the original runtime. (If this solution is less efficient than your original solution, include both and label the strech solution with a comment)


### Rubric

#### SEARCH

- DFS or BFS pass tests: 10 points

#### NAMES

- Optimize with an O(n log n) runtime solution: 8 points
- Optimize with an O(n) runtime solution: 10 points

#### COMPLEXITY

- One point each: 8 points

#### STRETCH

- Both DFS and BFS pass tests: 2 points
- `names.py` is optimized with sub-quadratic runtime complexity and tightly constrained linear space complexity: 2 points


#### GRADING

* *3*: 28+
* *2*: 20-17
* *1*: 0-19
