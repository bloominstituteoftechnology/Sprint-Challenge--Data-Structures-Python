# Import external libraries, modules:
import os
import time

# Import internal libraries, modules:
from binary_search_tree.binary_search_tree import BSTNode


# Time it:
start_time = time.time()

# Check for current directory, to make sure we search for files in the right directory:
dir = os.getcwd()
if dir.split('/')[-1] == "names":
    folder_name = ""
elif dir.split('/')[-1] == "Sprint-Challenge--Data-Structures-Python":
    folder_name = "names/"

# Get names from provided .txt files:
with open(folder_name + "names_1.txt", "r") as file:
    names_1 = file.read().split("\n")  # Read names from first list

with open(folder_name + "names_2.txt", "r") as file:
    names_2 = file.read().split("\n")  # Read names from first list

duplicates = []  # Return the list of duplicates in this data structure

# Populate BST tree with names in name list #1 (names_1):
# Runtime: O(nlogn)

# Start with a root node in the middle of the alphabet, to make the tree more balanced 
# (since no time to implement AVL tree class here now):
bst = BSTNode("Nn")
# Add rest of names
for name in names_1:
    bst.insert(name)

# Search for duplicates from names list #2 (names_2):
# Runtime: O(nlogn)
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
