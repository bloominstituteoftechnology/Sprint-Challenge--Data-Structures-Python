import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        ### Notice no return values, because we don't need to send anything up
        ### to original caller. Insert call isn't returning anything.
        #
        # Check if incoming node's value is less than the current node's value
        if value < self.value:
            # we know we need to go left
            # how do we know when we need to recurse again
            # or when to stop?
            if not self.left:
                # we can part our value here
                self.left = BSTNode(value)
            else:
                # we can't park here
                self.left.insert(value)
        else:
            # we know we need to go right
            if not self.right:
                # we can part our value here
                self.right = BSTNode(value)
            else:
                # we can't park here
                self.right.insert(value)

    def dupes(self, target):
    # When we start searching, self will be the root
    # compare the target against self
    #
    # criteria for returning False: we need to go either left 
    # or right, but there isn't another value in thar dir
        if target == self.value:
            # When this happens, the return True cascades up
            return duplicates.append(target)
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.dupes(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.dupes(target)

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


start_time = time.time()


duplicates = []

BST = BSTNode(names_1[0])

for name_1 in names_1[1:]:
    BST.insert(name_1)

for name_2 in names_2:
    BST.dupes(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
