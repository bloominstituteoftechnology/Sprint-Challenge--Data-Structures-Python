import time


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print(f"runtime: {end_time - start_time} seconds")


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.duplicates = []

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if self.value == value:
            duplicates.append(value)
        elif (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value


duplicates = []
names_1_set = set(names_1)
names_2_set = set(names_2)

firstName = names_1_set.pop()

bst = BinarySearchTree(firstName)
for name in names_1_set:
    bst.insert(name)

for name in names_2_set:
    bst.insert(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

"""
# Use my way, contains is now O(log n)
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = BinarySearchTree(value)

        def rec(target, current_node):
            if target > current_node.value:
                if current_node.right is None:
                    current_node.right = node
                    return
                else:
                    rec(target, current_node.right)
            elif target < current_node.value:
                if current_node.left is None:
                    current_node.left = node
                    return
                else:
                    rec(target, current_node.left)

        return rec(value, self)

    def contains(self, target):
        def rec(value, current_node):
            if current_node is None:
                return False
            elif value == current_node.value:
                return True
            elif value > current_node.value:
                return rec(value, current_node.right)
            elif value < current_node.value:
                return rec(value, current_node.left)

        return rec(target, self)

    def get_max(self):
        maxValue = -float("inf")
        current_node = self
        while current_node is not None:
            if current_node.value > maxValue:
                maxValue = current_node.value
            current_node = current_node.right

        return maxValue


duplicates = []

firstName = names_2[0]

bst = BinarySearchTree(firstName)

for name in names_2:
    bst.insert(name)

for name in names_1:
    if bst.contains(name):
        duplicates.append(name)
"""
