import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value > self.value: # then it belongs on the right
            if self.right is None: # so if there is room on the right
                self.right = BinarySearchTree(value) # extend a branch there
            else: # but if there isn't room
                self.right.insert(value) # move right and try again
        elif value < self.value: # then it belongs on the left
            if self.left is None: # so if there is room on the left
                self.left = BinarySearchTree(value) # extend a branch there
            else: # but if there isn't room
                self.left.insert(value) # move left and try again
            
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: # if this is the target we're looking for
            return True # success!
        elif target > self.value: # then it belongs on the right
            if self.right is None: # so if there isn't anything on the right
                return False # it isn't there
            else: # but if there is stuff on the right
                return self.right.contains(target) # check the right
        elif target < self.value: # then it belongs on the left
            if self.left is None: # so if there isn't anything on the left
                return False # it isn't there
            else: # but if there is stuff on the left
                return self.left.contains(target) # check the left

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None: # if there's nothing to the right
            return self.value # this is the maximum value
        else: # but if there is something to the right
            return self.right.get_max() # it's on the right, so check there

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value) # call the function cb for the current value
        if self.right is not None: # and if there's anything to the right
            self.right.for_each(cb) # apply this for_each function to the right
        if self.left is not None: # and if there's anything to the left
            self.left.for_each(cb) # apply this for_each function to the left

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Due to the double for-loop, the runtime complexity for the code commented out
# below is O(n^2);
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

duplicates = []
bst = BinarySearchTree(names_1[0])
for i in range(1, len(names_1)):
    bst.insert(names_1[i])
for i in range(len(names_2)):
    if bst.contains(names_2[i]):
        duplicates.append(names_2[i])
# The above runs under a second, but not under one hundredth of a second.

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
