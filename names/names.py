import sys
import time

from binary_search_tree import BinarySearchTree

sys.path.append("names/")

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# # Time Complexity: O(n^2)
# # Comment out for accurate runtime when testing Binary Search Tree solution.
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Using Binary Search Tree from module challenge. Time Complexity: O(n log n)
nameTree = BinarySearchTree(names_1[0])
for name in [names_1[i] for i in (1, -1)]:
    nameTree.insert(name)

duplicates = []
for name in names_2:
    if nameTree.contains(name):
        duplicates.append(name)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
