Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
  `O(1)` - Because our ring buffer observes semantics equivalent to a stack,
  the append operation has constant time complexity. For comparison, our
  `current` variable is equivalent to the PC or IP register, whereas out `storage`
  variable is equivalent to RAM.

2. What is the space complexity of your ring buffer's `append` function?
   `O(1)` - In the scope of `append`, two variables are reference, hence
   the memory occupied by the `append` method's (virtual) stack frame will
   remain constant independent of other variables.
   
   is, because our `Ringbuffer(n)` is implemented to have constant
   size determined at initialization, it'll only ever occupy `n` 'units' of space.

3. What is the runtime complexity of your ring buffer's `get` method?
   `O(n)` - To yield the `storage` of the `RingBuffer` and exclude any `None` values,
   we have to check the entirety of `storage` as we can't know (in very the naive
   case, which is what I implemented) where the `None` values are. Hence, for a
   `RingBuffer(n)` we'll iterate `n` times.

4. What is the space complexity of your ring buffer's `get` method?
   `O(n)` - The `get` method can occupy some `n` units of memory
   commensurate to the amount of non-`None` values in the `storage`
   variable. 

5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
