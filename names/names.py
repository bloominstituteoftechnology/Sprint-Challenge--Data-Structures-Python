'''
Program that compares the two lists (names_1.txt and names_2.txt) and returns a list of duplicated names.
Names appearing in both files will be stored in duplicates array.
'''

# Insert the names from list 1 into a search tree - import from class work
# Use the contains method to check if the tree contains the name in list 2

from binary_search_tree import BSTNode
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


'''
Runtime of 10.86 seconds. Runtime is O(n^2) - Quadratic time
Nested loops take as long as the length of list 1 * the length of list 2
'''

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Insert the names_1 data into a BST
# Use the first name to create the root node of the BST
tree = BSTNode(names_1[0])

# Insert the rest of the names into the existing BST
for name in names_1:        # O(n) to insert each each name from name_1 into the tree
    tree.insert(name)

# Check to see if the tree contains the names from list 2
for name in names_2:        # O(n) to go through each name in names_2 list

    # If the tree contains the name, append to duplicates list
    if tree.contains(name):             # O(log n) to check if the tree contains the name
        duplicates.append(name)     

'''
Runtime of 0.17413 seconds. Runtime complexity is O(n log n)
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# Using pythons method set()

# set1 = set(names_1)
# set2 = set(names_2)

# duplicates_2 = set1.intersection(set2)

# end_time = time.time()
# print (f"{len(duplicates_2)}")
# print (f"runtime: {end_time - start_time} seconds")

'''
Runtime is 0.00498. Runtime complexity is O(n)
Linear: it is dependant only on the length of the smaller list
'''