import time
from binary_search_tree import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
""" #MVP
bst = BSTNode("Root")

for e in names_2:
    bst.insert(e) #Binary search tree

while len(names_1) > 0:
    name_1 = names_1.pop() #Stack

    if bst.contains(name_1):
        duplicates.append(name_1)
"""



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#This is the array-only stretch
while len(names_1) > 0:
    name_1 = names_1.pop() #Stack - ish

    for name_2 in names_2:
        if(name_1 == name_2):
            duplicates.append(name_1)

        index += 1



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
