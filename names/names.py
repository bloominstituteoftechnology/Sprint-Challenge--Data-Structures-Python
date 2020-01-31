import time
from BinarySearchTree import BinarySearchTree

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
bst = BinarySearchTree(names_1[0])
for i in range(1, len(names_1)-1):
    bst.insert(names_1[i])

for name in names_2:
    if (bst.contains(name)):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


for name_1 in names_1:
    # for name_2 in names_2: 
    # By commenting out this line, runtime went from 13 secs to 2 secs
    # Original runtime of O(n^2) and I made it O(n).
    if name_1 in names_2:
        duplicates.append(name_1)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
