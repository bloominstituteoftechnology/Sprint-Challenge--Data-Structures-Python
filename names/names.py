import time

# importing binary search tree created earlier in the week


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
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)

        if self.left != None:
            self.left.for_each(cb)

        if self.right != None:
            self.right.for_each(cb)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

tree = BinarySearchTree(names_1[0])
for i in range(1, len(names_1)):
    tree.insert(names_1[i])

for i in names_2:
    if tree.contains(i):
        duplicates.append(i)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# without restriction, using a dictionary to get the runtime under one second
# first run time  6.808804273605347 seconds
# current run time 0.1519937515258789 seconds
# run time using a dictionary run time 0.006999492645263672 seconds
# this makes time complexity go from O(2n) to O(n)
