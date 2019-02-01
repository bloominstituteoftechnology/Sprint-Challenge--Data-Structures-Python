import time
from collections import defaultdict

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
d = defaultdict(int)
for name in names_1:
    d[name] += 1
for name in names_2:
    if d[name]:
        duplicates.append(name)

    
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

#https://docs.python.org/3/library/collections.html
#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

#hash table, dictionary look up, python built in sets are hash underhood, binary search tree
#put all names from names2 into BST
#for each name in names 1 check if name is in BST
#if so add to duplicates