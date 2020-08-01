import time

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

class BSTNode:
    def __init__(self, value):
        self.value = value
        # less than value
        self.left = None
        # greater than value
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == value:
            self.right = BSTNode(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        self.value = fn(self.value)

        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

bst_names_2 = BSTNode('blah')
for name_2 in names_2:
    bst_names_2.insert(name_2)

# Replace the nested for loops below with your improvements
def original():
    # My initial runtime was 1.6918909549713135 seconds
    # Runtime complexity: 0(n^2)
    for name_1 in names_1:
        for name_2 in names_2:
            if name_1 == name_2:
                duplicates.append(name_1)

def set_theory():
    # 0.0012035369873046875 seconds
    global duplicates
    duplicates = list(set(names_1).intersection(set(names_2)))

def bst_attempt():
    # 0.027079343795776367 seconds
    for name_1 in names_1:
        if bst_names_2.contains(name_1):
            duplicates.append(name_1)

start_time = time.time() # I moved this because I only want to test the
# processing of the data, not how long it takes to ingest to a list, and convert
# from a list to another data structuer.  Why would anyone do that, ingest 
# directly to the data structure you need.

# original()
set_theory()
# bst_attempt()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
