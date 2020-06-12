import time
from binary_search_tree import BSTNode
# adding the BST method to achieve better time and performance
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# runtime : 9.938354969024658 seconds


# def remove(duplicates):
duplicates = []  # Return the list of duplicates in this data structure
    # for name in duplicates:
        # if name is not duplicates:
            # duplicates.append(name)
        # return duplicates
        # print(remove(duplicates))

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

# Using BSTNode method
# runtime: 0.1481339931788037 seconds

# set the tree as the BSTNode for the first list of names
tree = BSTNode(names_1[0])
# add every name in names_1 to the BST
for name in names_1:
    tree.insert(name)
# check to see if our first name in names_1 is included in names_2
for name in names_2:
    if tree.contains(name):
# add an append method to duplicates with the value name
        duplicates.append(name)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
