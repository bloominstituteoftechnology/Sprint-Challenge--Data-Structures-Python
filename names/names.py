import time
from lru_cache import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#This solution runs in .015 seconds Run time complexity O(N), Old colde was O(n^2)
#Part 1: O(n)
# Create an LRU Cache with a limit of 10,000
lru = LRUCache(10000)
#For each name in the first list, add it to he cache with a key of the name, and a value of true
for name in names_1:
    lru.set(name, True)

#Part 2: O(n)
#  Loop through the names in the 2nd list
for name in names_2:
    #If the LRU get function find the name, it puts it at the end, saving a little time each search
    if lru.get(name) != None:
        #Adds the found duplicate name to the list 
        duplicates.append(name)


# Replace the nested for loops below with your improvements
# Old Code
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
