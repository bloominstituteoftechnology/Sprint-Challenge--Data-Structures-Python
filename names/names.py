import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# prev runtime is O(n^2)

# take a set of both list and return the similar names with python functions

# set1 = set(names_1)
# set2 = set(names_2)
# names = set1.intersection(set2)
# duplicates = [name for name in names ]

end_time = time.time()
# I did not read the directions clearly, so now i gotta implement Binary search, touche lambda
from binary_search_tree import BinarySearchTree

bst = BinarySearchTree(names_1[0])
[bst.insert(n) for n in names_1]

# for n in names_2:
#     duplicates.append(n) if bst.contains(n) == True else duplicates.append('')

for n in names_2:
    if bst.contains(n):
        duplicates.append(n) 
# new intersect search is O(n log n)

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
