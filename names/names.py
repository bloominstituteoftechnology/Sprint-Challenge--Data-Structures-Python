from binary_search_tree import BinarySearchTree
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

"""
O(n**2)
time: 7.434
due to nested loops
"""
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


"""
0(n log n)
Time: 0.139
no nested loop
using bst
names_1 still dependent on n + additional work
names_2 dropped to log n
might be O(2n log n) since we still loop through both names arr
"""
bst = BinarySearchTree(names_1[0])
for count, name_1 in enumerate(names_1):
    if count == 0:
        continue
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
