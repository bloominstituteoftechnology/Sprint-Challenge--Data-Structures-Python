"""
Task 2. Runtime Optimization
"""

import bisect
import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names

duplicates_1 = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements.
# The starter code is O(n^2).
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

name_tree = BinarySearchTree(names_2[0])
for name in names_2[1:]:
    name_tree.insert(name)

for name in names_1:
    if name_tree.contains(name):
        duplicates_1.append(name)

end_time = time.time()
print(f"BST runtime: {end_time - start_time} seconds\n")

# ---------- Stretch Goal #1 -----------
# Python has built-in tools that allow for a very efficient approach to this
# problem. What's the best time you can accomplish? Thare are no restrictions
# on techniques or data structures, but you may not import any additional
# libraries that you did not write yourself.


start_time = time.time()

for _ in range(100):
    duplicates_2 = set(names_1).intersection(set(names_2))

end_time = time.time()

print(f"Set runtime: {(end_time - start_time) / 100} seconds\n")

# ---------- Stretch Goal #2 -----------
# Say your code from names.py is to run on an embedded computer with very
# limited RAM. Because of this, memory is extremely constrained and you are
# only allowed to store names in arrays (i.e. Python lists). How would you go
# about optimizing the code under these conditions? Try it out and compare
# your solution to the original runtime. (If this solution is less efficient
# than your original solution, include both and label the strech solution with
# a comment.)

start_time = time.time()

duplicates_3 = []
names_1 = sorted(names_1)

def index(searchable, target):
    """
    Helper function. Locates the leftmost value exactly equal to x.

    Note that this is not original code; it's a standard solution to a
    standard problem!
    """
    i = bisect.bisect_left(searchable, target)
    if i != len(searchable) and searchable[i] == target:
        return i
    raise ValueError

for name in names_2:
    try:
        index(names_1, name)
        duplicates_3.append(name)
    except ValueError:
        pass

end_time = time.time()
print(f"Sort & bisect runtime: {end_time - start_time} seconds\n")

# Sanity check - we should find the same 64 names in all three solutions.
assert set(duplicates_1) == set(duplicates_2)
assert set(duplicates_2) == set(duplicates_3)

sorted_dupes = sorted(duplicates_3, key=lambda x: tuple(x.split()[::-1]))

print(f"{len(duplicates_3)} duplicates:\n\n{', '.join(sorted_dupes)}")
