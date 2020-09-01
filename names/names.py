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
## NOTE: Before BST implementation my first run time was 10.12610387802124 seconds
## COOLER NOTE: After BST implementation my run time is 9.32251501083374 seconds

# Replace the nested for loops below with your improvements

bst = BSTNode("None")
duplicates = []

for name in names_1:
    bst.insertValue(name)
for name in names_2:
     if bst.containsTarget(name):
         duplicates.append(name)

bst = BSTNode("None")
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
        
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n{', '.join(duplicates)}\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

