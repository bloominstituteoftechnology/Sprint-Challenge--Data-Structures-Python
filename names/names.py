import time
import sys
sys.path.append('../imports')
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# ORIGINAL CODE: O(n^2) runtime of 5.327 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# IMPROVED CODE: O(n) runtime of 0.109 seconds
# Put the 2nd list of names into a BST
# Then append matches to duplicates list as before.
names2_tree = BinarySearchTree(names_2[0])

for name in names_2:
    names2_tree.insert(name)

for index in range(1, len(names_1)):
    if names2_tree.contains(names_1[index]):
        duplicates.append(names_1[index])


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
