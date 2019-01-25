Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

   - The run time complexity is O(n) because the operation runs once per node
     in the binary search tree.

2. What is the space complexity of your `depth_first_for_each` function?

   - To my knowledge the addition of the `depth_first_for_each` method is only
     adding O(1) constant space. Binary search itself needs to create a new object for each node
     costing O(n) space. The callback function can have a wide range of effects
     on space complexity, but this challenge is independant of the callback.

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?

5) What is the runtime complexity of the provided code in `names.py`?

   - The run time complexity of the provided nested for loop solution is O(n\*\*2).
     the nested portion of the for loop becomes a power factor to the next operation.

```
# NESTED FOR LOOPS

# duplicates = []                           O(1)
# for name_1 in names_1:                    O(n)
#     for name_2 in names_2:                O(n)
#         if name_1 == name_2:              O(1)
#             duplicates.append(name_1)     O(1)

# TOTAL                                     O(n**2)
# nested for runtime    6.037697076797485 seconds

```

6. What is the space complexity of the provided code in `names.py`?

   - The space complexity of the provided code is O(n). This is mainly affected
     by the initial creation of the 10,000 item array. The variables declared
     in a for loop are destroyed when they go out of scope causing them to add
     only constant space O(1) which is neglegable compared to O(n)

7) What is the runtime complexity of your optimized code in `names.py`?
   - The total runtime complexity is `O(n log n)` The dominant scaling factors in runtime complexity for the binary
     search tree option, are the 2 for loops. These alone would be O(2n) if we did
     not drop the constants to O(n). Nested in the second loop is a O(log n) because
     we divide and conquer. For each name in the first list we divide and conquer against the second.

```
# BINARY SEARCH TREE

duplicates = []                             # O(1)
# Set up one list in binary search tree
bst = BinarySearchTree(names_2[0])          # O(1)
for name_2 in names_2[1:]:                  # O(n)
    bst.insert(name_2)                      # O(1)

# Loop through next list and use bst to see
# if it is a duplicate. If so append to
# duplicates array
for name_1 in names_1:                      # O(n)
    if bst.contains(name_1):                # O(log n)
        duplicates.append(name_1)           # O(1)

# TOTAL                                     O(n log n)
# Binary search runtime    0.10671377182006836 seconds
```

8. What is the space complexity of your optimized code in `names.py`?
   - The space complexity of this method is `O(n)`. Creating the arrays from
     each list is O(n), and the creation of the pinary search tree is another
     O(n) space. This leads to a complexity of O(3n) but of course we drop the
     constants again.
