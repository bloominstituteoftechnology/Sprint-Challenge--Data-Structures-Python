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

# Replace the nested for loops below with your improvements
# tree = BinarySearchTree(names_1[0])
# for name in names_1:  # 0.27 sec, O(n log n), n to create the tree + n to touch each name in 2 * log n to check
#     tree.insert(name)
# for name in names_2:
#     if tree.contains(name):
#         duplicates.append(name)
# for name_1 in names_1:
#     if name_1 in names_2:  # 1.08 sec O(n)? This assumes the check for "in" is constant time, but it must not be
#         duplicates.append(name_1)
    # for name_2 in names_2:  # 9.7 sec O(n^2)
    #     if name_1 == name_2:
    #         duplicates.append(name_1)

""" Stretch """
set_1 = set(names_1)  # 0.00359 sec pretty sure this is constant time
set_2 = set(names_2)
duplicates = set_1.intersection(set_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
