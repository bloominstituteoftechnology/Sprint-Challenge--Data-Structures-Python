import time
import sys



start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Ivan Here --- The original code is O(n^2) complexity due to nested for loops. 
# I think Binary Search Tree is perfect for this.
# I will import it and use 'contains' method:

from bin_search_tree import BSTNode

bst = BSTNode("")

for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

# This now runs with a runtime on my machine of ~.1 seconds.

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
