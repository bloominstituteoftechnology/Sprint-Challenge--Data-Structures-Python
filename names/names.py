
#runtime: 0.23733282089233398 seconds

import time
from BST import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Using a BST to cut the time
head = names_1[0]
names_1 = names_1[1:]

bst = BSTNode(head)

for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
    
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#runtime: 0.004609107971191406 seconds

start_time = time.time()

f = open('names_1.txt', 'r')
names_3 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_4 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates1 = []  # Return the list of duplicates in this data structure

def intersection(lst1, lst2): 
    temp = set(lst2) 
    lst3 = [value for value in lst1 if value in temp] 
    return lst3

duplicates1 = intersection(names_3,names_4)

end_time = time.time()
print (f"{len(duplicates1)} duplicates:\n\n{', '.join(duplicates1)}\n\n")
print (f"runtime: {end_time - start_time} seconds")