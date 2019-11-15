import time
from bst_names import BST

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# This runtime is O(n^2)
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

start_time2 = time.time()
root = BST('names')
for name2 in names_2:
    root.insert(name2)

duplicates2 = []
for name_1 in names_1:
    if root.contains(name_1):
        duplicates2.append(name_1)

end_time2 = time.time()
print (f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n")
print (f"runtime: {end_time2 - start_time2} seconds")
