import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names/names_1.txt', 'r')
all_names = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
all_names += f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name in all_names:
    if all_names.count(name) > 1 and name not in duplicates:
        duplicates.append(name)
    else:
        continue

end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")