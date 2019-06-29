import time
from bst import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# This will return the duplicates while checking both files
duplicates = list(set(names_1) & set(names_2))

# This will return if there is existing duplicates in one file
# bst = BinarySearchTree([names_1[0], 1], [names_2[0], 1])
# duplicates = []
# def callback(i):
#     if i[1] >= 2:
#         duplicates.append(i[0])


# for i in range(1, len(names_1)-1):
#     bst.insert([names_1[i], 1, 1])
# for j in names_2:
#     bst.insert([j, 1, 2])

# bst.for_each(callback)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
