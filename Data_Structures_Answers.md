Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
    O(1) Constant time because n has no bearing on the runtime.

2. What is the space complexity of your ring buffer's `append` function?
    O(n) where n is the buffer's initial capacity

3. What is the runtime complexity of your ring buffer's `get` method?
    O(n) because the for loop has to go through every value in our buffer

4. What is the space complexity of your ring buffer's `get` method?
    Best case is O(n) but worse case would be O(2n) because the array used to 
    store non-None values could be filled with every element in our storage

5. What is the runtime complexity of the provided code in `names.py`?
    O(n^2) because of the nested for loop.

6. What is the space complexity of the provided code in `names.py`?
    O(3n) at worst because each name in the files may be duplicated which means
    we'd then have to store each value 3 times as the size of n grows.

7. What is the runtime complexity of your optimized code in `names.py`?
    O(n 2log(n)) because it is O(log(n)) for insertion of our names into the tree,
    then again O(log(n)) for comparison and then O(n) for insertion into our list.

8. What is the space complexity of your optimized code in `names.py`?
    Best case would be O(n) if no duplicates found and worst case would be O(2n) if every single element is duplicated because we would need first to store it in a tree then again in our list. 