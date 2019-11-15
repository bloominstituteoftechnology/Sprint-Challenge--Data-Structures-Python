import time
from lru_cache import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

cache = LRUCache(10000)
[cache.set(x, x) for x in names_2]
print(f'names2 size {len(names_2)} and cache size {cache.current_nodes}')

duplicates = []
for name_1 in names_1:
    if cache.get(name_1) is not None:
        duplicates.append(name_1)
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

