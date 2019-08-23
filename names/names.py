import time
from binarysearch import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Original code -- Runtime: 12.05 seconds:
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Optimized code using a BST -- Runtime: 0.19s
bst = None

for name1 in names_1:
    if bst is None:
        bst = BinarySearchTree(name1)
    else:
        bst.insert(name1)

duplicates = []

for name2 in names_2:
    if bst.contains(name2):
        duplicates.append(name2)

# Code for stretch -- Runtime: 2.43s:
# names = [name1 for name1 in names_1]

# duplicates = []

# for name2 in names_2:
#     if name2 in names:
#         duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

