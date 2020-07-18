import time
from binary_search_tree import BSTNode

duplicates = []  # Return the list of duplicates in this data structure

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

tree = None
tree2 = None

#loop over names 1
for name in names_1:
    #for first name create a bstnode w that value
    if tree is None:
        tree = BSTNode(name)
    else:
        #for every name after, call insert on that bstnode
        tree.insert(name)
#call method to return sorted list of names
# tree.in_order_print(None)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#for the first name in names_2 create a bstnode using that value
for name in names_2:
    #the first time we loop through we initialize BSTNode(name) and the result was we inserted the name
    result = "added"
    if tree2 is None:
        tree2 = BSTNode(name)

    #if it is not the first name
    else:
        #and if we are not inserting a duplicate name from names_2
        result = tree2.insert(name)

    if result != "duplicate":

        #and if the name exists in names_1
        if tree.insert(name) == "duplicate":
            duplicates.append(name)

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
