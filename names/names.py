import time
from binary import BSTNode 
# from collections import deque


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

# O(n^2) for loop within a four loop

# O(n log n) due to bigger list its log n

# binary search tree for the list

# original runtime: 6.412154197692871 

binary = BSTNode(names_1[0]) #runtime: 0.10668492317199707 seconds

for name in names_1: # checks if name is in list 
    binary.insert(name)

for name in names_2: #checks if name is in list 
    if binary.contains(name): 
        duplicates.append(name) # appends duplicates



# Space complexity	O(n) + O(m)	O(n)

# Time complexity	O(n) + O(m) + O(m*n)


#stretch

# collections = deque(names_1[0])

# for name in names_1:
#     collections.append(name)

# for name in names_2:
#     if collections.contains(name):
#         duplicates.append(name)

# set_1 = set(names_1)                        # runtime: 0.004072904586791992 seconds
# set_2 = set(names_2)

# duplicates = set_1.intersection(set_2)

# cast each input list to a set
# a set in Python is an unordered collection with no duplicate elements
# sets have an intersection method to return unique elements found in both sets  
# intersection_set = set1.intersection(set2)
# cast intersection_set as list
# return list
# https://dfrieds.com/python/intersection-two-arrays.html


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
