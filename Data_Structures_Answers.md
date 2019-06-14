Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

        The worst-case runtime capacity of this method is O(n). This is because the first if statement needs to loop through the array, in the worst case it will loop through the whole array. Same with the next line that is trying to find the first index of None. It loops through twice in a row there.
        
2. What is the space complexity of your ring buffer's `append` function?

        The space complexity of this method is O(1). I will assign each property once and there is no recursion.

3. What is the runtime complexity of your ring buffer's `get` method?

        The runtime complexity of this method is O(n). In the worst case the list comprehension in the first line will need to iterate over every element in the list.

4. What is the space complexity of your ring buffer's `get` method?
        
        The space complexity of this method is O(1), for the same reason as for the `append` method.


5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
