Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   Constant time, all i am doing is popping or inserting to the top, without making the list all over again.
2. What is the space complexity of your ring buffer's `append` function?
   Pretty sure this is constant too, as we are not making extra arrays but are in place.
3. What is the runtime complexity of your ring buffer's `get` method?
   <!-- Constant time, we always have as many items to call as the capacity allows,  -->
   Actually, come to think of it, this is probably linear time, as we pass in the capacity at the beginning of the argument.
   It doesn't get larger than the capacity, so I am not sure how to answer this, but if we take into consideration
   that the get() method will always be constant with the capacity, and we need to list all items in the array, you can argue
   this method takes linear time.
4. What is the space complexity of your ring buffer's `get` method?
   Constant space, all we are doing is calling the list with that capacity amount.

5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
