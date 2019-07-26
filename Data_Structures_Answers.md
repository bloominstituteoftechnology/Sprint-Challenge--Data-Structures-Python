Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

   `O(1)` - Because our ring buffer observes semantics equivalent to a stack,
   the append operation has constant time complexity. For comparison, our
   `current` variable is equivalent to the PC or IP register, whereas out `storage`
   variable is equivalent to RAM.

2. What is the space complexity of your ring buffer's `append` function?

   `O(1)` - In the scope of `append`, two variables are referenced, hence
   the memory occupied by the `append` method's (virtual) stack frame will
   remain constant independent of other variables.
   
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

   `O((j+k)+(j*k)) = O(n*m)` - As we have two lists of arbitrary size where for each
   element in one, we iterate through the other list entirely, and each is 
   being read in from a file. We have to read through a file of variables size
   `j` and another of variable size `k`.

6. What is the space complexity of the provided code in `names.py`?

   `O(j+k) = O(n)` - The programs size in memory varys wrt to the data loaded
   in from the files, hence we have linear space complexity. 

7. What is the runtime complexity of your optimized code in `names.py`?

   `O(n)` - Because search a trie has (average) time complexity of `O(n)`
   where `n` is the length of the string, and insertion into a trie has
   time complexity of `O(m)` because - again - we're only doing as many
   operations as there are characters in a string of length `m`. 

8. What is the space complexity of your optimized code in `names.py`?
   `O(n)`
