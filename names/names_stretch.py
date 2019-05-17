import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

all_names = names_1 + names_2

duplicates = [name for name in names_1 if names_1.count(name) > 1]

end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")