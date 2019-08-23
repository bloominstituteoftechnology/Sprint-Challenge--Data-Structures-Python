import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# #MVP ----------------------------------------------------------------------------

# tree = BinarySearchTree([names_1[0], 1])
# duplicates = []
# def cb(x):
#     if x[1] >= 2:
#         duplicates.append(x[0])

# for i in range(1, len(names_1)-1):
#     tree.insert([names_1[i], 1, 1])
# for j in names_2:
#     tree.insert([j, 1, 2])

# tree.for_each(cb)

#MVP ------------------------------------------------------------------------------

#stretch --------------------------------------------------------------------------

duplicates = []

names_1.sort()
names_2.sort()

j = len(names_1)-2
while j >= 0:
    if names_1[j] == names_1[j+1]:
        del names_1[j+1]
    j -= 1

z = len(names_2)-2
while z >= 0:
    if names_2[z] == names_2[z+1]:
        del names_2[z+1]
    z -= 1

duplicates.extend(names_1)
duplicates.extend(names_2)
duplicates.sort()

i = len(duplicates)-1
while i >= 0:
    if i+1 > len(duplicates)-1 and duplicates[i] != duplicates[i-1]:
        duplicates[i] = None
        i -= 1
    elif i-1 < 0 and duplicates[i] != duplicates[i+1]:
        duplicates[i] = None
        i -= 1
    elif duplicates[i] != duplicates[i-1] and duplicates[i] != duplicates[i+1]:
        duplicates[i] = None
        i -= 1
    elif duplicates[i] == duplicates[i-1]:
        duplicates[i-1] = None
        i -= 1
    elif duplicates[i] == duplicates[i+1]:
        duplicates[i] = None
        i -= 1

for j in range(len(duplicates)-1, -1, -1):
    if duplicates[j] == None:
        del duplicates[j]

#stretch --------------------------------------------------------------------------

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"{len(duplicates)}")
print(f"runtime: {end_time - start_time} seconds")


