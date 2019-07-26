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

   `O(j+k) = O(n)` - The program's size in memory varys wrt to the data loaded
   in from the two files whose size we can denote with `j` and `k`. This simplifies
   in Big-O to just `n`, hence we have linear space complexity. 

7. What is the runtime complexity of your optimized code in `names.py`?

   `O(n)` - Because:
     - Trie search has (average) time complexity of `O(n)`
     - Trie insertion has time complexity of `O(m)`

   where in each case only `n` operations ever occur varying with the length of 
   the given string. And, because we iterate over `names_1` of size `j` and then
   over `names_2` of size `k`, we get the sequential operations of 
   `O(n) + O(m) + O(j) + O(k)` which rounds to `O(n)`.

8. What is the space complexity of your optimized code in `names.py`?

   `O(j*k)` - Given that:
     - `names_1` is of size `n`
     - `names_2` is of size `m`
     - A trie is of (average) size `j*k`, for `j` words and an average word length of `k` 

    We can deteremine that the code has a space complexity of: `O(n) + O(m) + O(j*k)` for
    an average complexity of `O(j*k)` 
