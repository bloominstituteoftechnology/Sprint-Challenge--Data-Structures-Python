import time

# copy pasta BST (binary search tree) we did in the lesson

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

    def insert(self, value):
        if self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif self.value >= value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif self.right and self.value < target:
            return self.right.contains(target)
        elif self.left and self.value > target:
            return self.left.contains(target)
        else: 
            return False

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else: 
            return self.value

    def for_each(self, cb):
        cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

tree = BinarySearchTree(name_1[0])
for i in range(1, len(name_1)):
    tree.insert(name_1[i])

for i in name_2:
    if tree.contains(i):
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
