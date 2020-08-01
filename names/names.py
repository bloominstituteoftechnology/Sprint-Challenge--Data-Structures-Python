import time
from bstclass import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Populate a binary search tree containing the 'names_2' list's contents
bst_names_2 = BSTNode(names_2[0])
for nme in names_2:
    bst_names_2.insert(nme)

# Iterate through the 'names_1' list and see if a duplicate exists
for nme in names_1:
    # Does the BST structure contain the name being processed?
    if bst_names_2.contains(nme):
        # Match found -> add to our duplicates list
        duplicates.append(nme)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
