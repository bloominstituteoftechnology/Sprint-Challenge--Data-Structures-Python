import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# these iterative approaches are wasting resources. Because we're searching, the thought of using a binary search tree comes to mind.
# that would speed up our runtime and wast less resources
# the runtime complexity of the code below is O(n*n) = O(n^2)
# exponential runtime is only going to get worse with scale.
# binary search tree could have a runtime complexity of O(log(n))

# commenting out code
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# instantiating the class
# required argument for a value. We can put the first value of one of the lists
bst = BinarySearchTree(names_1[0])

# we can put one txt file of names in the binary search tree
# then use the contains method of the bst to see if names from the second file are duplicates
# if they are, we append them to the duplicates list

for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did
# not write yourself.
