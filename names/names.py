import time

# next time I need to read more closely


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

# n1 = names_1
# n2 = names_2


duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

names_tree = BinarySearchTree(names_1[0])
for i in range(1, len(names_1)):
    names_tree.insert(names_1[i])

for i in names_2:
    if names_tree.contains(i):
        duplicates.append(i)

# originally 7 seconds before making this O(2n) = 0(n)
# duplicates = set(n1) & set(n2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
