Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(n). It goes through the length of the array and saves it in temp.
If the array is less than capacity, it performs a swap operation on each item.
If the array is at capacity, the oldest item is swapped.

2. What is the space complexity of your ring buffer's `append` function?

O(2n) which is simplified to O(n). We save the length of the array twice - once in get and once in self-storage.

3. What is the runtime complexity of your ring buffer's `get` method?

O(n). The for loop goes through the entire array.

4. What is the space complexity of your ring buffer's `get` method?

O(n) - it saves the array in temp.

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2). It has a nested for loop which means it's n squared.

6. What is the space complexity of the provided code in `names.py`?

O(log n). It saves only the duplicated names.

7. What is the runtime complexity of your optimized code in `names.py`?

O(log n). I used the in built timsort algorithm to sort one of the arrays. I then used Binary Search for O (log n) solution. This is because it can dismiss half of the array at each operation if the target string is larger (alphabetically) to the midpoint string.

8. What is the space complexity of your optimized code in `names.py`?

O(n). The first array is saved once, then sorted and saved again. We then check for duplicates in the second array. If there is a duplicate, we save it to the duplicates array.
