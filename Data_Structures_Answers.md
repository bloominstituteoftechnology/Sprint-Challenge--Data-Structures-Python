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

        The runtime complexity of the provided code is O(n * m). This is because for every item in `names_1` list that I am iterating over, I am also iterating over every item in `names_2`. In this case, that means I am iterating 10,000*10,000 times. Because they're the same number of iterations, it's basically O(n^2).



6. What is the space complexity of the provided code in `names.py`?

        The space complexity of the provided code is O(n). This is because in worst case we are going to be storing an `n` amount of elements in the duplicates array.

7. What is the runtime complexity of your optimized code in `names.py`?
        
        The runtime complexity of my optimized code is O(n). I am still running two for loops, but they are not nested. On line 19 I am seeing if `name_2` is inside a dictionary that I created of `name_1` names. I know that accessing a dictionary value is an O(1) operation, and I'm going out on a limb here to guess that seeing if the dictionary contains a value is also an O(1) operation, and that the dictionary does not have to iterate over values to do perform the operation.

8. What is the space complexity of your optimized code in `names.py`?
        
        The space complexity of my optimized code is still O(n). I am using a bit more memory than in the provided code due to my dictionary also being filled in the worst case with `n` elements.
