import time
from BST import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

BSTNode = BSTNode(names_1[0]) # initialize BST
#A given leaf node (a letter from the alphabet) of the optimal alphabetic binary search tree can be located using a binary search procedure. The latter does not hold for optimal alphabetic tree. Algorithms for building optimal alphabetic trees can be used to build optimal alphabetic binary search trees.
for name in names_1:
    BSTNode.insert(name)

for name in names_2:
    if BSTNode.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.