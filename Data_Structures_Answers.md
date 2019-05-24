Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1)

2. What is the space complexity of your ring buffer's `append` function?
I would argue O(1) because I access the space(memory) in the array directly,
as opposed to O(n). 

3. What is the runtime complexity of your ring buffer's `get` method?
O(n), because I have to iterate through the entire array one by one.

4. What is the space complexity of your ring buffer's `get` method?
O(n), same as above.

5. What is the runtime complexity of the provided code in `names.py`?
The provide code used a nested for loop. O(n^2) || O(n * m) 
where n is name in names_1, and m is name in names_2. 

6. What is the space complexity of the provided code in `names.py`?
O(n)

7. What is the runtime complexity of your optimized code in `names.py`?
O(n)

8. What is the space complexity of your optimized code in `names.py`?
O(n)