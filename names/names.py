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
# label bst as the first name in names_1 txt file
bst = BSTNode(names_1[0])

"""
we are going to insert the name for the name in first
txt file if name isn't equal to first name in name_1 index
"""
[bst.insert(name) for name in names_1 if name != names_1[0]]
# checking for duplicates - returned 64
[duplicates.append(name) for name in names_2 if bst.contains(name)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# my runtime shows from PowerShell:
# runtime: 0.09596920013427734 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
