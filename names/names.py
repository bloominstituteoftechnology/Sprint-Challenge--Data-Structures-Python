import time
from BST import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
#create a variable to hold reference the binary tree class
bst = BinarySearchTree(names_1[0])

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# #loop through the names in names_1 file...
for names_1 in names_1:
    #use insert method from bst to add the names from from names_1 file 
    bst.insert(names_1)
    
    #loop through names in names_2 file 
for names_2 in names_2:
    #using the contains bst method, check if it contains names 
    if bst.contains(names_2):
        #if it does, add the names_1 names to duplicates array 
        duplicates.append(names_1)







end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
