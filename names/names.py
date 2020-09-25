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

# Replace the nested for loops below with your improvements (orginal time took ~3.5 sec(forgot to copy it))

bst = BinarySearchTree(names_1[0])

# for x in names_1:
#     bst.insert(x)

# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)

# runtime: 0.061672210693359375 seconds

names2_dict = {}

for name in names_2:
    names2_dict[name] = 1

for name in names_1:
    if names2_dict.get(name) == None:
        pass
    else:
        duplicates.append(name)

# runtime: 0.00577545166015625 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


