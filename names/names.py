import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

both_names = names_1 + names_2
cache = dict()
duplicates = []

for name in both_names:
    try: 
        if cache[name] == 1:
            cache[name] += 1
            duplicates.append(name)
        elif cache[name] > 1:
            continue
    except KeyError as e:
        cache[name] = 1
        continue

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

