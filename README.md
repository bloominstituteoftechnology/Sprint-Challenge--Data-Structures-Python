# Sprint Challenge: Data Structures

In this week's Sprint you implemented some classic and fundamental data structures and learned about how to go about evaluating their respective runtimes and performance. This Sprint Challenge aims to assess your comfort with these topics through exercises that build on the data structures you implemented and the algorithmic intuition you've started to build up.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your Challenge score is a measure of your ability to work independently using the material covered throughout this sprint. You need to demonstrate proficiency in the concepts and objectives that were introduced and that you practiced in the preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL and Instructor in your cohort help channel on Slack. Your submitted work reflects your proficiency in the concepts and topics that were covered this week.

You have three hours to complete this Sprint Challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons) and it also helps your project manager to more thoroughly assess your work.

## Description

This Sprint Challenge is split into three parts:

1. Implement a data structure called a ring buffer (more details below)
2. Optimizing some inefficient code
3. Reversing the contents of a singly linked list

### Minimum Viable Product

#### Task 1. Implement a Ring Buffer Data Structure

A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds elements to the buffer. The `get` method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

_You may not use a Python List in your implementation of the `append` method (except for the stretch goal)_

*Stretch Goal*:  Another method of implementing a ring buffer uses an array (Python List) instead of a linked list.  What are the advantages and disadvantages of using this method?  What disadvantage normally found in arrays is overcome with this arrangement?

For example:

```python
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
```

#### Task 2. Runtime Optimization

***!Important!*** If you are running this using PowerShell by clicking on the green play button, you will get an error that `names1.txt` is not found.  To resolve this, run it, get the error, then `cd` into the `names` directory in the `python` terminal that opens in VSCode.

Navigate into the `names` directory. Here you will find two text files containing 10,000 names each, along with a program `names.py` that compares the two files and prints out duplicate name entries. Try running the code with `python3 names.py`. Be patient because it might take a while: approximately six seconds on my laptop. What is the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the code. Can you get the runtime to under a second? Under one hundredth of a second?

*You may not use the built in Python list, set, or dictionary in your solution for this problem.  However, you can and should use the provided `duplicates` list to return your solution.*

(Hint: You might try importing a data structure you built during the week)


#### Task 3. Reverse a Linked List

Inside of the `reverse` directory, you'll find a basic implementation of a Singly Linked List. _Without_ making it a Doubly Linked List (adding a tail attribute), complete the `reverse_list()` function within `reverse/reverse.py` reverse the contents of the list. 

For example,
```
1->2->3->None
```
would become...
```
3->2->1->None
```

While credit will be given for a functional solution, only optimal solutions will earn a ***3*** on this task.

#### Stretch 

* Say your code from `names.py` is to run on an embedded computer with very limited RAM. Because of this, memory is extremely constrained and you are only allowed to store names in arrays (i.e. Python lists). How would you go about optimizing the code under these conditions? Try it out and compare your solution to the original runtime. (If this solution is less efficient than your original solution, include both and label the strech solution with a comment)


### Rubric
| OBJECTIVE | TASK | 1 - DOES NOT MEET Expectations | 2 - MEETS Expectations | 3 - EXCEEDS Expectations | SCORE |
| ---------- | ----- | ------- | ------- | ------- | -- |
| _Student should be able to construct a queue and stack and justify the decision to use a linked list instead of an array._ | Task 1. Implement a Ring Buffer Data Structure | Solution in `ring_buffer.py` DOES NOT run OR it runs but has multiple logical errors, failing 3 or more tests | Solution in `ring_buffer.py` runs, but may have one or two logical errors; passes at least 7/9 tests | Solution in `ring_buffer.py` has no syntax or logical errors and passes 9/9 tests | |
| _Student should be able to construct a binary search tree class that can perform basic operations with O(log n) runtime._ | Task 2. Runtime Optimization | Student does NOT correctly identify the runtime of the starter code in `name.py` and optimize it to run in under 6 seconds | Student does not identify the runtime of the starter code in `name.py`, but optimizes it to run in under 6 seconds, with a solution of O(n log n) or better | Student does BOTH correctly identify the runtime of the starter code in `name.py` and optimizes it to run in under 6 seconds, with a solution of 0(n log n) or better |  |
| _Student should be able to construct a linked list and compare the runtime of operations to an array to make the optimal choice between them._ | Task 3. Reverse the contents of a Singly Linked List | Student's solution in `reverse.py` is failing one or more tests | Student's solution in `reverse.py` is able to correctly print out the contents of the Linked List in reverse order, passing all tests, BUT, the runtime of their solution is not optimal (requires looping through the list more than once) | Student's solution in `reverse.py` is able to correctly print out the contents of the Linked List in reverse order, passing all tests AND it has a runtime of O(n) or better |  |
| _Student should be able to write code that utilizes Python Collections_ | [STRETCH] Optimize code from Task 2, given the constraint that **only standard Python collections** may be used to store names | Level 1 solution provided | Level 2 solution provided | Level 3 solution provided |  |
| **FINAL SCORE** | _(3 tasks + 1 STRETCH goal)_  | **0-5** | **6-9** | **10-12** |  |


#### Passing the Sprint
Score ranges for a 1, 2, and 3 are shown in the rubric above. For a student to have _passed_ a sprint challenge, they need to earn an **average of at least 2** for all items on the rubric.
