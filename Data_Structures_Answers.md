Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   The append method is O(n). For each item that we have I'm looping through the array once to check if it has any None's in it.
   If it does have a None in it, it goes through an O(1) operation of pop and O(1) operation of append. If it doesn't have any None's in it,
   then I'm just setting the item to the storage place of the oldest added item and
   incrementing the current variable; none of that increases time complexity.

2. What is the space complexity of your ring buffer's `append` function?
   Space complexity of the append method is also O(n). We're just deining one array
   and looping through it. The operations that we perform on the array don't grow
   the array, they only remove and add items to the end and beginning of the array.

3. What is the runtime complexity of your ring buffer's `get` method?
   The get method is also O(n). For each item in the array I'm looping through it once with one for loop. I'm checking if there are no None's in the array and then I'm either appending, which again is an O(1) operation, or returning an empty
   array. I also printed the self.storage out just to see how many times the loop is
   run each time the method is called and it's just n where n is the length of the array.

4. What is the space complexity of your ring buffer's `get` method?
   The get method space complexity is worst case O(2n). It's 2n because I'm defining a new array and then appending items into it. So for each n items in the array I've got the original array plus the new array which is an array with all None values in it which I"m returning.

5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
