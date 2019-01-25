import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# NESTED FOR LOOPS

# duplicates = []                           O(1)
# for name_1 in names_1:                    O(n)
#     for name_2 in names_2:                O(n)
#         if name_1 == name_2:              O(1)
#             duplicates.append(name_1)     O(1)

# TOTAL                                     O(n**2)
# nested for runtime    6.037697076797485 seconds


# BINARY SEARCH TREE

duplicates = []                             # O(1)
# Set up one list in binary search tree
bst = BinarySearchTree(names_2[0])          # O(1)
for name_2 in names_2[1:]:                  # O(n)
    bst.insert(name_2)                      # O(1)

# Loop through next list and use bst to see
# if it is a duplicate. If so append to
# duplicates array
for name_1 in names_1:                      # O(n)
    if bst.contains(name_1):                # O(log n)
        duplicates.append(name_1)           # O(1)

# TOTAL                                     O(n log n)
# Binary search runtime    0.10671377182006836 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

