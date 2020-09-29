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

# for name_1 in names_1:
#     if name_1  in names_2:
#         duplicates.append(name_1)
from bst import BSTNode

# CREATE TREE WITH names_1 LIST
start_time = time.time()

tree = BSTNode(names_1[0])
for name in names_1:
    tree.insert(name)

duplicates = [name for name in names_2 if tree.contains(name)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------




# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# LIST COMPREHENSION
# ~ 1.5 seconds which is def better than the original

# CREATE TREE WITH names_2 LIST (just in case order is better)
# ... it's not
start_time = time.time()

tree = BSTNode(names_2[0])
for name in names_2:
    tree.insert(name)

duplicates = [name for name in names_1 if tree.contains(name)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")




# USING SETS

