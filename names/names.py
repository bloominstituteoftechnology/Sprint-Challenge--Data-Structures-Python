import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
"""
You may not use the built in Python list, set, or dictionary in your solution for
this problem. However, you can and should use the provided duplicates list to
return your solution.
"""
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ABW Solution II: using binary search tree (solution I was a fail!)
bst = BinarySearchTree("A")

for x in names_1:
    bst.insert(x)

for y in names_2:
    if bst.contains(y):
        duplicates.append(bst.contains(y))


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# Time on First Run: 5.129 seconds
# Time on ABW Solution II: 0.111 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did
# not write yourself.


# if __name__ == "__main__":
#     my_list = [1,2,3,4]
#     other_list = [5,2,7,4]
#     dupes = []

#     for i,x in product(my_list, other_list):
#         if i == x:
#             dupes.append(i)

#     print(dupes)
#     # breakpoint()
