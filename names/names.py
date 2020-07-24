import time
from binary_search_tree import BinarySearchTree

tree = None

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

### 0.17504072189331055

# for name in names_1:
#     if tree:
#         tree.insert(name)
#     else:
#         tree = BinarySearchTree(name)

# for name in names_2:
#     if tree.contains(name):
#         duplicates.append(name)



##### 1.9464917182922363

# for name in names_1:
#     if names_2.count(name) >= 1:
#         duplicates.append(name)



### 2.0965280532836914

# for name in names_1:
#     if name not in names_2:
#         pass
#     else:
#         duplicates.append(name)



### 0.024008512496948242   BUT COUNTS 124 DUPLICATES

setOne = set()
for name in names_1:
    if name not in setOne:
        setOne.add(name)
for name in names_2:
    if name in setOne:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
