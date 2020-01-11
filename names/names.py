import time
from bst import BinarySearchTree

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# ---------- my code without using list, dict, or set -----------
start_time1 = time.time()
duplicates = []
bst = BinarySearchTree('duplicate_names')
#add all names from names_1 to a binary search tree
for name in names_1:
    bst.insert(name)
#check each name in names_2 to see if it exists in the tree
for name in names_2:
    #if it does, append it to the dulicates array
    if bst.contains(name):
        duplicates.append(name)

end_time1 = time.time()
print (f"duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"{len(duplicates)} duplicates | runtime for bst: {end_time1 - start_time1} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

#same concept as above; except with a dictionary instead of a binary search tree
start_time2 = time.time()
duplicates = []
dict = {}
for name in names_1:
    dict[name] = None
for name in names_2:
    if name in dict:
        duplicates.append(name)
end_time2 = time.time()
print (f"{len(duplicates)} duplicates | runtime for dict stretch: {end_time2 - start_time2} seconds")

start_time3 = time.time()
fast_duplicates = set(names_1+names_2)
end_time3 = time.time()
print (f"{len(duplicates)} duplicates | runtime for set stretch: {end_time3 - start_time3} seconds")

# ---------- Stretch Goal -----------
#Say your code from `names.py` is to run on an embedded computer with very limited RAM.
#Because of this, memory is extremely constrained and you are only allowed to store names in arrays (i.e. Python lists).
#How would you go about optimizing the code under these conditions? Try it out and compare your solution to the original runtime.
#(If this solution is less efficient than your original solution, include both and label the strech solution with a comment)
start_time4 = time.time()
duplicates = []
for name in names_1:
    if names_2.count(name) >= 1:
        duplicates.append(name)
end_time4 = time.time()
print (f"{len(duplicates)} duplicates | runtime for array stretch: {end_time4 - start_time4} seconds")

# ---------- Original for reference -----------
start_time5 = time.time()
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
end_time5 = time.time()
print (f"{len(duplicates)} duplicates | runtime for original: {end_time5 - start_time5} seconds")