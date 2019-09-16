import time
from binary_search_tree import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

########## Defult Search Code #########

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

############# MVP Search ###########

# names = BinarySearchTree(names_1[0])
# for i in names_1:
#     names.insert(i)
# for index in range(len(names_2)):
#     if names.contains(names_2[index]):
#         duplicates.append(names_2[index])

# average runtime 0.09 - 0.10

########### Stretch ##########

duplicates = [names_2[x] for x in range(len(names_2)) if names_2[x] in names_1]

# average runtime 0.9 - 1.0 seconds





end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
