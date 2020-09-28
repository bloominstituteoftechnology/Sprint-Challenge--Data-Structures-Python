import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names/names_1.txt', 'r')
# List containing 10000 names
names_1 = f.read().split("\n")  
f.close()

f = open('names/names_2.txt', 'r')
# List containing 10000 names
names_2 = f.read().split("\n")  
f.close()

duplicates = []

# Replace the nested for loops below with your improvements
root = names_1[0]
names_1_bst = BSTNode(root)

# loop through 
for name in names_1[1:]:
    #add names to a binary search tree
    names_1_bst.insert(name)
  
for name in names_2:
    if names_1_bst.contains(name):
        duplicates.append(name)

end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.