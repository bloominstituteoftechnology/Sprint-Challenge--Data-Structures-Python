import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
bst_node = BSTNode("")

# We'll need to loop through all the names in 'names_1' file
for name in names_1:
    # use the 'insert' method to add each name
    bst_node.insert(name)

# Loop through all the names in 'name_2' file
for name in names_2:
    # Use an if statement to check if the tree has identical names 
    if bst_node.contains(name):
        # in the case it does, append those names to the duplicated list
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
