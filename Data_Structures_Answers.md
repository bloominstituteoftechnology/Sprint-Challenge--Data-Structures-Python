Add your answers to the questions below 

1. What is the runtime complexity of your ring buffer's `append` method?

O = 1

2. What is the space complexity of your ring buffer's `append` function?

O = 1 up to the max capacity since the space will remain the same since we are over-writing the oldest element once max capacity is reached

3. What is the runtime complexity of your ring buffer's `get` method?

O = O(n) since the each element will be added to the list comprehension.

4. What is the space complexity of your ring buffer's `get` method?

O(n) since it will be as big as the ring buffer since it needs to return each element.

5. What is the runtime complexity of the provided code in `names.py`?

0=n^2

6. What is the space complexity of the provided code in `names.py`?

O = n 

7. What is the runtime complexity of your optimized code in `names.py`?

the runtime O = (len1)log(len2) which is better than what it was before.

8. What is the space complexity of your optimized code in `names.py`?

O =n 
