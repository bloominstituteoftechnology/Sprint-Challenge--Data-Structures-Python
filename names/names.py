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

'''
runtime: 10.171310663223267 seconds
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

#Initiallizing binary search tree node
bst = BSTNode("")

#inserting names from list 1 into node 
for name in names_1:
    bst.insert(name)


#checking if the 2nd list contains names from the bstnode using contains method
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
#runtime: 0.10272502899169922 seconds


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# def compare_intersect(x, y):
#     return frozenset(x).intersection(y)

# stretch_duplicates = [x for x in names_1 if x in names_2]
#runtime: 0.0029883384704589844 seconds


#stretch_duplicates = compare_intersect(names_1, names_2)
#runtime: 0.0029921531677246094 seconds
# print (f"{len(stretch_duplicates)} duplicates:\n\n{', '.join(stretch_duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")