Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

2. What is the space complexity of your `depth_first_for_each` function?

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?

The original runtime complexity here is O(n ^ 2) due to the nested loop:

duplicates = []
    for name_1 in names_1:
        for name_2 in names_2:
            if name_1 == name_2:
                duplicates.append(name_1)

With the way this is set up, we have to check our names_2 list for every single time we iterate through the names_1 list in order to check for equivalency. Thus, for every new entry into our input, we'll have to run two checks: one to iterate through names_1 and a second to perform the equivalency check via names_2.

6. What is the space complexity of the provided code in `names.py`?

The space complexity is the same as the optimized version of the code, O(n). The required storage space will scale linearly with the number of entries. It will not scale exponentially like the runtime since there are no further operations to be performed.

7. What is the runtime complexity of your optimized code in `names.py`?

The runtime complexity of the optimized code is O(n) due to the use of a hash table. Since the only operation being used is a simple check to see whether a particular name is at a particular index, the growth is linear. We do not have to adjust our runtime based on the size of the single_names set since the only relevant number is the input size. Input size alone will always determine the number of iterations and therefore the runtime.

8. What is the space complexity of your optimized code in `names.py`?

The space complexity is also O(n), again because we're simply storing values that are related to the number of inputs. This is why hash tables are not necessarily the most space-efficient solution, but since our concern here was runtime it is a highly effective solution.