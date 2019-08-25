import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

''' 
Orignal code needed to be replaced


duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

#New code start
duplicates = []
names_1_tree=BinarySearchTree(names_1[0])
for i in range(1,len(names_1)):
    names_1_tree.insert(names_1[i])

for i in names_2:
    if names_1_tree.contains(i):
        duplicates.append(i)





end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

