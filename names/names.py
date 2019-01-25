import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        direction = 'right' if value > self.value else 'left'
        if getattr(self, direction) is not None:
            self = getattr(self, direction)
        else:
            setattr(self, direction, BinarySearchTree(value))
            return value
        return self.insert(value)

    def contains(self, value):
        direction = 'right' if value > self.value else 'left'
        if self.value is not None and self.value != value and getattr(self, direction) is not None:
            self = getattr(self, direction)
        elif self.value is not None and self.value == value:
            return True
        else:
            return False
        return self.contains(value)

    def get_max(self):
        r = 'right'
        if self.value is not None and getattr(self, r) is not None:
            self = getattr(self, r)
        elif self.value is not None and getattr(self, r) is None:
            return self.value
        return self.get_max()


binary_list = BinarySearchTree(names_1[0])
# needed the [0] to declare the initial value
for i in names_1:
    binary_list.insert(i)
# Declares and inputs values into the Binary tree ^
duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# for i in range(0, 10000):
#     if names_1[i] in names_2:
#         duplicates.append(names_1[i])
    # Better but not the best takes about 1.16 seconds
    # Binary search tree would make second half of function faster
for i in names_2:
    if binary_list.contains(i):
        duplicates.append(i)
# This finishes in about 0.1 seconds for me
# Probably the best I'm gonna get


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

