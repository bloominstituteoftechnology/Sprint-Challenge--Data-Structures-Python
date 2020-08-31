import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#
# Original: 10.36 seconds -- O(n**2) Quadratic
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#
# Method 1: 1.94 seconds
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)
#
# Method 2: 1.89 seconds <-- stretch method. Names only in lists
# duplicates = [name for name in names_1 if name in names_2]
#
# Method 3: 0.00647 seconds <-- Best method if sets are available
# name_set = set(names_1)
# duplicates = list(name_set - name_set.difference(set(names_2)))

# Method 4: 0.163 seconds <-- using our data structures
tree = BSTNode(None)
for name in names_1:
    tree.insert(name.lower())
for name in names_2:
    if tree.contains(name.lower()):
        duplicates.append(name)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
