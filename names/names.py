
import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# runtime: 10 seconds, runtime complexity: O(n**2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# use Binary Search Tree to go through and search duplicates using contains
# Runtime ~.25, Runtime complexity O(log(n))
# a = BSTNode("")
# bst = BSTNode(names_1[0])

# for name in names_1:
#     a.insert(name)

# for name2 in names_2:
#     if a.contains(name2):
#         duplicates.append(name2)


# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


names_table = {}

for name in names_1:
    names_table[names] = True

for name in names_2:
    if name in names_table:
        duplicates.append(name)


end_time = time.time()
print("\n\n\nList Version:")
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
