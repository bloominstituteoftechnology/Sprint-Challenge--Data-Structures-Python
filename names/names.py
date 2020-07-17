import time


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: Value is less than self.value
        if value < self.value:
            # If there is no left child, then insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # Else: ????
                # Repeat the process on left subtree
                # self.left.insert(value)
            else:
                self.left.insert(value)

        # Case 2: Value is greater than or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Case 1: self.value == target
        if self.value == target:
            return True
        # Case 2: if target is less than self.value

        found = False

        if self.value >= target:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            found = self.left.contains(target)
        # Case 3: otherwise
        if self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

  # Return the maximum value found in the tree
    def get_max(self):
        if self is None:
            return None
        # Forget about the left subtree altogether
        # Iterate through the nodes using a loop construct
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

    # Recursive version of get_max() method
    def get_max_(self):
        if self.right is None:
            return self.value
        return self.right.get_max_()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

new_names = None

for name1 in names_1:
    if not new_names:
        new_names = BSTNode(name1)
    new_names.insert(name1)

for name2 in names_2:
    if new_names.contains(name2):
        duplicates.append(name2)

# The first for loop will be O(n) runtime due to a 1:1 correlation of size of inputs to
# the number of operations performed, i.e. the number of operations performed is directly
# proportional to the number of names in the first list

# The runtime complexity for the second for loop should be O(log n) since we are using a
# binary search tree data structure and utilizing the sorting/search properties of a tree

# The resulting runtime complexity will be O(n) + O(log(n)) = O(n). The overall runtime for the
# sum of these operations will be O(n) or the superior bound in this equation due to the fact
# that we are assessing the worst case scenario. However, utilizing the seek properties of of a
# BST allows us to increase dramatically the overall runtime over the original operation
# which utilized nested for loops with an overall complexity of O(n) + O(n) = O(n)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
