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
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

""" 
my code implementation, after test, had a runtime of .12772s returning 64 dup names from both names list

"""

nodes = BSTNode('')

for name_1 in names_1:
    nodes.insert(name_1) 

for dupe_names in names_2:
    if nodes.contains(dupe_names):
        duplicates.append(dupe_names)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

print(f"{len(set(names_1) & set(names_2))} duplicates using built-in-tool set: {set(names_1) & set(names_2)}")
print (f"runtime: {end_time - start_time} seconds, which is much faster compared to the previous code's runtime: 0.1678149700164795 seconds, and the original code's runtime: 11.417479038238525 seconds")