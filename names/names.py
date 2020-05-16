import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# initialize BST
bts_1 = BinarySearchTree('')

# add names from first list to binary search tree
# Run Time Complexity is O(n * log(n)) ? 
for name in names_1:
    #O(log(n))
    bts_1.insert(name)

#Stretch
# set1 = set(names_1)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#Stretch
# set2 = set(names_2)

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# Run Time Complexity is O(n^2)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# iterates through first list
# Run Time Complexity is O(n * log(n))
for name in names_2:
    # checks if name is in b tree O(log(n))?
    if bts_1.contains(name):
        # adds name to duplicates list if returns True
        duplicates.append(name)

#Stretch
# Big O(n) sets run at O(1) per value
# duplicates = set1.intersection(set2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# By using built in intersection method on sets I was able to bring the run time
# Down from 0.38s to 0.0129s. I was lucky enough to stumble upon this method by googling intersection python method
# instead of using btree or O(n^2) nested loop original solution, this is much faster. Wasn't expecting such a huge difference
