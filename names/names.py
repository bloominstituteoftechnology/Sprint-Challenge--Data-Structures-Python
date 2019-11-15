import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
bst = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    print(name)
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
# duplicates = [name for name in names_1 if name in names_2]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

