Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
 - O(n) since it has to go through each of the items

2. What is the space complexity of your `depth_first_for_each` function?
 - O(1) because no new variables or constants are being created. Unless python creates a new variable when one is passed into a function, then it would be O(n) since I use recursion, but I don't believe that happens.

3. What is the runtime complexity of your `breadth_first_for_each` method?
 - O(n) since it has to go through each of the items

4. What is the space complexity of your `breadth_first_for_each` method?
 - O(n) since all but the first node are being added to a deque

5. What is the runtime complexity of the provided code in `names.py`?
 - O(n^2) because of the nested for loop
	 - (O(n^2 + n) without dropping less important time complexities - n from reading the files)

6. What is the space complexity of the provided code in `names.py`?
 - O(n) since the names in the files weren't stored anywhere other than the initial lists composed when the filea were read 
	 - (O(n + duplicates) without dropping less important space complexities)

7. What is the runtime complexity of your optimized code in `names.py`?
 - O(n)
	 - (O(2n) without dropping less important time complexities - 1n from reading, n/2 from turning names1 into a dict, and n/2 from checking names2 against names_1)

8. What is the space complexity of your optimized code in `names.py`?
 - O(n) since I create a dictionary with each of the 1000 names in names_1 
	 - (O((3n)/2 + duplicates) without dropping less important space complexities - 1n from reading the files)
