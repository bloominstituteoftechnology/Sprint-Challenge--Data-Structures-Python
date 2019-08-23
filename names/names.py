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
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''
duplicates = []

namesTree1 = BinarySearchTree(names_1[0])
namesTree2 = BinarySearchTree(names_2[0])

for x in names_1:
    namesTree1.insert(x)
#for y in names_2:
#    namesTree2.insert(y)

for name in names_2:
    if namesTree1.contains(name):
        duplicates.append(name)

end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

'''
cb = lambda x: print(x)
namesTree1.for_each(cb)
'''