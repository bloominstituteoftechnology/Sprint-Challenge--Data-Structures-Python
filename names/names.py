import time
import sys
# sys.path.append('../reverse/')
from binary_search_tree import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# **** Run time ****
# Original algorithm as runtime O(n^2)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# names = sorted(names_1 + names_2)
# i = 0
# while i < len(names)-1:
#     if names[i] == names[i+1]:
#         duplicates.append(names[i])
#         i += 2
#     else:
#         i += 1

# ll = LinkedList()

# for name in names_1:
#     ll.add_to_head(name)
# for name in names_2:
#     if ll.contains(name):
#         duplicates.append(name)

tree = BinarySearchTree(names_1[1])
for name in names_1[1::]:
    tree.insert(name)

for name in names_2:
    if tree.contains(name):
        duplicates.append(name)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)