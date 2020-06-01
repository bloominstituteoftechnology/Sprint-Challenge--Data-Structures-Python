import time


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

    # Insert the given value into the tree only if it does not already exist,
    # else append to the duplicates list
    def insert_originals_only(self, value):
        if value >= self.value:
            if self.right:
                if value == self.right.value:
                    duplicates.append(value)
                else:
                    self.right.insert_originals_only(value)
            else:
                self.right = BSTNode(value)
        else:
            if self.left:
                if value == self.left.value:
                    duplicates.append(value)
                else:
                    self.left.insert_originals_only(value)
            else:
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is target:
            return True

        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False


start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# First attempt - O(n): avg time ~0.85 sec
# for name_1 in names_1:
#     if names_2.__contains__(name_1):
#         duplicates.append(name_1)


# Second attempt - O(log n): avg time ~0-.072 sec
# name_tree = BSTNode("")

# for name in names_1:
#     name_tree.insert_originals_only(name)

# for name in names_2:
#     name_tree.insert_originals_only(name)


# Third O(n): ~0.85 sec
# duplicates = [name for name in names_1 if name in names_2]

duplicates = (set(names_1) + set(names_2)) - (set(names_1) - set(names_2))

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
