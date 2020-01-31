import time
from lru_cache import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


#### New code (0.08 seconds, complexity = O(n)) #######
# creating empty list of duplicates
duplicates = []

# add all names in names_1 to lru cache
lru = LRUCache(10000)
for name in names_1:
    lru.set(name, True)

# loop through names_2 and add to duplicates if name in cache
for name in names_2:
    if lru.get(name) != None:
        duplicates.append(name)
#######################################################


#----- Old code (~ 10 seconds, complexity = O(n^2)) ------
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#---------------------------------------------------------

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
