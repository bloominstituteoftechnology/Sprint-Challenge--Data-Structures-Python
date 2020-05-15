import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


class BinaryTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, value):
        new_node = BinaryTree(value)
        # if we do not have a value yet
        if self.value == None:
            self.value = value
        # if our value is less than value go left
        elif value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.add_node(value)
        else:
            if self.right is None:
                self.right = new_node
            else:
                self.right.add_node(value)

    def contains(self, target):
        # ! if taget equals the value then append that value to duplicates
        if target == self.value:
            duplicates.append(target)
        # ! if target is less than the value, go left
        if target < self.value:
            # ! if left is none stop searching
            if self.left is None:
                return None
            # ! else recursivly restart the search from the left node (restart the process from this node)
            else:
                self.left.contains(target)
        # ! else if target is greater than the value, go right
        else:
            # ! if right node is none, stop searching
            if self.right is None:
                return None
            # ! else recursivly restart the search from the right node (restart the process from this node)
            else:
                self.right.contains(target)


# test = BinaryTree()
# for name in names_1:
#     test.add_node(name)
# for name in names_2:
#     test.contains(name)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ! Stretch Solution using Set
name1 = list(set(names_1))
name2 = list(set(names_2))
names = sorted(name1 + name2)
for i in range(len(names) - 1):
    if names[i] == names[i + 1]:
        duplicates.append(names[i])
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
