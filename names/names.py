import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
tree = BinarySearchTree(names_1[0])
for i in names_1[1:]:
    tree.insert(i)




f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
start_time2 = time.time()
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
#print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(len(duplicates))
print (f"runtime for loop only: {end_time - start_time2} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


#This solution is not allows according to the README, but I left is just becuase it is how I would normally do it. 
#See the real solution below

start_inter = time.time()
a = set(names_1)
b = set(names_2)

c = list(a.intersection(b))
end_time = time.time()

print(len(c))

print (f"runtime for intersection: {end_time - start_inter} seconds")

if set(c) == set(duplicates):
    print(True)


# Real solution using binary search tree

start_inter = time.time()
dubs = []

for i in names_2:
    state = tree.contains(i)
    if state == True:
        dubs.append(i)
end_time = time.time()
print(len(dubs))
print (f"runtime for Binary Tree Search: {end_time - start_inter} seconds")
