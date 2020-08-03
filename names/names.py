import time

start_time = time.time()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left else False
        else:
            return self.right.contains(target) if self.right else False

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# runtime: 2.8881919384002686 seconds
def nested_loops():
    for name_1 in names_1:
        for name_2 in names_2:
            if name_1 == name_2:
                duplicates.append(name_1)

# runtime: 0.0057239532470703125 seconds
def set_intersection():
    global duplicates
    duplicates = list(set(names_1).intersection(set(names_2)))

# runtime: 0.1219017505645752 seconds
def bst():
    bst_names = BSTNode('Names')
    for name in names_1:
        bst_names.insert(name)
    for name in names_2:
        if bst_names.contains(name):
            duplicates.append(name)

# nested_loops()
set_intersection()
# bst()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
