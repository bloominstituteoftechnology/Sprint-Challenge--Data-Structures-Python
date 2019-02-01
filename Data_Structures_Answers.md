Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
	
	It is O(n); because we're calling the method exactly once per node, and since there are "n" nodes, it is O(n) operation.

2. What is the space complexity of your `depth_first_for_each` function?

	It is O(1) because we're not allocating any new data structures.

3. What is the runtime complexity of your `breadth_first_for_each` method?

	It is O(n) because we're looping once per node.

4. What is the space complexity of your `breadth_first_for_each` method?

	There are two scenarios:
	The best case is there is only one item in the queue and we get what we want right away, so it is O(1).
	The worse case takes a little more explaining; pretty much we would need to figure out how many items are in the last depth (row) of the binary tree, and compare that value to the total number of items in the tree.
	
			A
		B		C
	  D	  E	  F	  G  <-- last row = 4 items
						 total items = 7
						
						=> last is roughly 1/2 of the (total + 1)
						
		** Find the operation:		last = (total + 1) / 2
		
	===> So the worse case is O((n + 1) / 2) => O(n).
	
5. What is the runtime complexity of the provided code in `names.py`?
	
	It is O(n^2) because we have a loop inside a loop, and each loop is O(n).
	It took 5.364984035491943 seconds to run this solution.
	
6. What is the space complexity of the provided code in `names.py`?
	
	Here, there are two scenarios:
	The worse case is every name is a duplicate, so it's O(n).
	The best case is there are no duplicates, so it's O(1).

7. What is the runtime complexity of your optimized code in `names.py`?

	The solution I implemented uses a set(), and break out of the loop inside loop structure, so the runtime complexity is O(2 * n) => O(n).
	It took 0.005104780197143555 seconds to run this solution, which is under one hundredth of a second like the instructions wanted.

8. What is the space complexity of your optimized code in `names.py`?

	There are two scenarios:
	To start off, this solution has a set(), so the space complexity is already at O(n).
	Then, we need to take a look at how everything else run together.
	The worse case is every name is a duplicate, so it's O(n), and O(n) + O(n) => O(2*n).
	The best case is there are no duplicates, so it's O(1), and O(1) + O(n) => O(n).
