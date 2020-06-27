import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Initial runtime of 6.28 seconds
# The nested loops result in a time complexity of O(n^2) which does not scale very well at all 

# A set could be created from the second array, then check the first array against the set
# If the set contains a name, one can simply append the name to duplicates

names_2_set = set(names_2)
duplicates = [name for name in names_1 if name in names_2_set]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# The result is a runtime of 0.00159 seconds
# By the use of hashing, the time complexity of the check for set membership is O(1) on average
# As compared to checking in a an array, like the first example was doing which is O(n)
# Therefore, we end up with an overall time complexity of O(n)
# This is only possible because the names are hashable, if they were not hashable
# we would need to use a method that sorts the names, such as inserting to a binary search tree
# This would still require that the elements be comparable, and would result
# in a time complexity of O(n log n), that is the best time that sorting can be done in

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
