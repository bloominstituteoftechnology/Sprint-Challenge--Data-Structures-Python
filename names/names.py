import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()


f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# Current runtime complexity: O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class NamesBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = NamesBST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = NamesBST(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

names_search_tree = NamesBST(names_1[0])
# Runtime complexity: O(n)
for name in names_1:
    names_search_tree.insert(name)

#Runtime complexity: O(log n)
for name in names_2:
    if names_search_tree.contains(name):
        duplicates.append(name)

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
