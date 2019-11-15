import time
# Initially ran 5.68 seconds

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# for name1 in names_1:  # for each item in names_1
#     for name2 in names_2:  # look at each item in names_2
#         if name1 == name2:  # if they're the same, append name1 to duplicates
#             duplicates.append(name1)

# This runtime is 1.028 seconds
# for item in names_1:
#     if item in names_2:
#         duplicates.append(item)

# Use set because it is useful to create lists that are
# made up of only unique values

# Using set has runtime of .0038 seconds
# duplicates = set(names_1) & set(names_2)
# find uniques at the intersection of the 2 lists

# Just saw that I can't use set or dictionary :( Used BST HW

# THIS RUNTIME IS 0.0938


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:  # value < self.value
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if target == self.value:
            return True

        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        else:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    def find_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max()


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# use names from names_1 in BST
BST = BinarySearchTree(names_2[0])
for i in names_1[1:]:
    BST.insert(i)

# Now find the dupes from names_1 in names_2
for name2 in names_2:
    if BST.contains(name2):
        duplicates.append(name2)
og_time = 5.58

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
print(f"Original runtime: {og_time} seconds\nImprovement of {og_time - (end_time - start_time)} seconds")
