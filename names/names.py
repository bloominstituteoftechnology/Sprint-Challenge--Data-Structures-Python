import time

# CREATE A BINARY SEARCH TREE DATA STRUCTURE FOR USE IN THIS PROBLEM:
class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# CONVERT THE LIST LISTS OF NAMES INTO A BINARY SEARCH TREE FOR FASTER LOOKUP BY:
BST = BinarySearchTree(names_2[0]) # INITIALIZE BST WITH FIRST NAME IN `names_2`
for name_1 in names_1[1:]: # SLICE `names_1`, STARTING FROM THE MIDDLE
    BST.insert(name_1) # INSERT THIS SLICE INTO THE BST

# FIND DUPLICATES OF `names_1` IN `names_2`, THEN APPEND THEM TO THE DUPLICATES LIST BY: 
for name_2 in names_2:
    if BST.contains(name_2): # COMPARE NAMES FROM `names_2` TO VALUES IN BST (WHICH NOW CONTAINS THE NAMES `names_1`)
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
