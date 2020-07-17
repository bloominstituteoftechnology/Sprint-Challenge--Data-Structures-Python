import time
from bst import BSTNode


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# CREATE TREE WITH names_1 LIST
start_time = time.time()

tree = BSTNode(names_1[0])
for name in names_1:
    tree.insert(name)

duplicates = [name for name in names_2 if tree.contains(name)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# CREATE TREE WITH names_2 LIST (just in case order is better)
# ... it's not. it's the same 
start_time = time.time()

tree = BSTNode(names_2[0])
for name in names_2:
    tree.insert(name)

duplicates = [name for name in names_1 if tree.contains(name)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# LIST COMPREHENSION
# ~ 1.5 seconds which is def better than the original

start_time = time.time()

duplicates = [name for name in names_1 if name in names_2]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# USING SETS

start_time = time.time()

duplicates = set(names_1) & set(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# DIFFERENT LIST COMPREHENSION
# For some reason introduces an order?
# this is fastest

start_time = time.time()

duplicates = [i for i, j in zip(names_1, names_2) if i==j]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")