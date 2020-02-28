import time
from binary_search_tree import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure


names_1_tree = BinarySearchTree(names_1[0])
# * iterator for inserting names into BST
name_idx = 1

# * inserts each name into BST
while name_idx <= len(names_1[1:]):
    names_1_tree.insert(names_1[name_idx])
    name_idx += 1

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# * use list comp to create list of matching names
# * run a binary search conains method on the names BST for every name in the * second * name list
duplicates = [name for name in names_2 if names_1_tree.contains(name)]

# * solves in just under .05 seconds.


# * intersection method
def record_intersections(l1, l2):
    intersections = [set(l1).intersection(l2)]
    return intersections
    # ** runs in .0040 seconds if l1 is a set and l2 is not a set, adds ~.001 seconds to convert both to set


second_list = record_intersections(names_1, names_2)

end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(second_list)
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
