import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Original Solution
# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#
# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# Time to complete this will be O(n log(n))
# First it goes through every name in names_1 and creates a Binary Search Tree from those names
# Second, it searches through each one, in the binary search tree which will yield Log(n) times

from binary_search_tree import BinarySearchTree

tree = BinarySearchTree(names_1[0])
for nme in names_1[1:]:
    tree.insert(nme)
dupes = []
for nme in names_2:
    if tree.contains(nme):
        dupes.append(nme)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# On my humble little laptop, The runtime of the original yields ~6.77 seconds
# The revised binary search tree version yields ~0.09 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# Had to come back to this one, because you know how much I love sets, LOL
# This further reduces the time to ~0.0018 seconds on my laptop

start_time = time.time()

dups = []
n2 = set(names_2)
for n in names_1:
    if n in n2:
        dups.append(n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")