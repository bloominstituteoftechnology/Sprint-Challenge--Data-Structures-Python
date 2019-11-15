import time
from lru_cache import LRUCache
from dll_stack import Stack

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = LRUCache(10000)
[names_1.set(x, x) for x in f.read().split("\n")] # List containing 10000 names
#save one list as an LRU cache
f.close()

f = open('names_2.txt', 'r')
# names_2 = Stack()
# [names_2.push(x) for x in f.read().split("\n")]  # List containing 10000 names
# save it as a stack

# names_2 = f.read().split("\n")

duplicates = [names_1.get(x) for x in f.read().split("\n") if names_1.get(x) is not None]

f.close()

# duplicates = []

# while names_2.len() > 0:
#     name = names_2.pop()
#     if names_1.get(name) is not None:
#         duplicates.append(name)

# for name in names_2:
#     if names_1.get(name) is not None:
#         duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

