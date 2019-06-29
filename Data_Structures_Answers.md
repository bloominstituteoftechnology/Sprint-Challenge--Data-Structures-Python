Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

   > This is O(1). Ring buffers must have a fixed length size at all times.

2. What is the space complexity of your ring buffer's `append` function?

   > This is also true here O(1) it only overwrites the oldest

3. What is the runtime complexity of your ring buffer's `get` method?

   > Again The ring buffers get method still will be an O(n)

4. What is the space complexity of your ring buffer's `get` method?

   > Because of using a loop this complexity will be O(n)

5. What is the runtime complexity of the provided code in `names.py`?
   > Since we where given the code it had nested for loop was O(n^2)
6. What is the space complexity of the provided code in `names.py`?
   > The provided code shows complexity of O(n)
7. What is the runtime complexity of your optimized code in `names.py`?
   > Since this is very optimized solution it is O(1) at worse it would be O(n)
8. What is the space complexity of your optimized code in `names.py`?
   > Again space here is O(1) would be at worse O(n)

For all time complexities on the List() function I checked the https://wiki.python.org/moin/TimeComplexity
This shows that At Worst the Set(Item) is O(n)
