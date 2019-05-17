Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
- O(1)
- The append function takes constant time to add an element to the array.

2. What is the space complexity of your ring buffer's `append` function?
- O(1)
- The append function only uses at most 1 space.

3. What is the runtime complexity of your ring buffer's `get` method?
- O(n)
- I have to do a for loop to 'n', which means that the ring buffer's get method is constant time.

4. What is the space complexity of your ring buffer's `get` method?
- O(n)
- In the worse case, I need to store 'n' values in the value_to_return array.

5. What is the runtime complexity of the provided code in `names.py`?
- O(n^2)
- In the original implementation of names.py, there was a double 'for' loop, so n^2.

6. What is the space complexity of the provided code in `names.py`?
- O(n/2)
- In the original implementation of names.py, in the worst case, all of the items would contain one duplicate. Thus a list of all of the duplicates would need to be kept. If there were 20,000 names, I would need to store 10,0000.

7. What is the runtime complexity of your optimized code in `names.py`?
- O(n)
- My implementation incorporates a cache (via a python dictionary). Looking up values in a cache is very efficient at O(1) time complexity. While the code still needs to visit n names, the code checks whether or not a key already exists in the dictionary of all previously reviewed names in O(1) or constant time.

8. What is the space complexity of your optimized code in `names.py`?
- O(n)
- My time complexity optimization came at a cost of space complexity. In the worst case scenario, in which all of the items contain one duplicate, I have to keep in storage the value of both the first reference and the duplicate, meaning that my space requirements have doubled relative to my previous implementation. If there were 20,000 names, I would need to store 10,0000 in the duplicates array and 10,000 in the cache.
