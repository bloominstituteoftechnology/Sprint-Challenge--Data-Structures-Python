from binary_search_tree import BSTNode
import time

# Using binary search tree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

names_2_tree = BSTNode(names_2[0])
for name in names_2[1:]:
    names_2_tree.insert(name)

duplicates = [name for name in names_1 if names_2_tree.contains(name)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# Using set

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

# Initial runtime of 6.29 seconds
# These nested loops result in a time complexity of O(n^2) which scales horribly


# We could create a set from the second array, then check the first array against the set
# If the set contains a name, we can simply append the name to duplicates

names_2_set = set(names_2)
duplicates = [name for name in names_1 if name in names_2_set]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# This results in a runtime of 0.0035 seconds
# By using hashing, the time complexity of the check for set membership is O(1) on average
# As compared to checking in a an array, like the first example was doing which is O(n)
# Therefore, we end up with an overall time complexity of O(n)
# This is only possible because the names are hashable, if they were not hashable
# we would need to use a method that sorts the names, such as inserting to a binary search tree
# This would still require that the elements be comparable, and would result
# in a time complexity of O(n log n), as that is the best time that sorting can be done in


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
