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

# We can implement a BST and the time will be reduced (I got down to 0.10918 seconds). 
# BST has a worst case time complexity of O(n), but average of O(log(n))

# bst = BSTNode("None")
# for name in names_1:
#     bst.insert(name)
# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)

# using sets and the built-in python function `intersection`, we can greatly reduce runtime down (I got 0.00444 seconds)
duplicates = set.intersection(set(names_1), set(names_2))
# this answers the stretch goal

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.