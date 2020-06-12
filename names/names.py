import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # LEFT
        if value < self.value:
            # if there's no node on the left, stop here and make a new node
            if not self.left:
                self.left = BSTNode(value)
            else:
                # keep searching
                self.left.insert(value)
    
        # RIGHT
        else:
            # if there's no node on the right, stop here and make a new node
            if not self.right:
                self.right = BSTNode(value)
            else:
                # keep searching
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
    
        # self is the starting point (root)
        # target is what we pass in to see if it's in the tree

        # return False if we know we need to go in one direction
        # but there's nothing in the left or right direction

        # once target is equal to our current node, we stop the recursion
        if target == self.value:
            return True

        # LEFT
        if target < self.value:
            # if we hit a dead end, that means the target isn't in the tree
            if not self.left:
                return False
            # if current node != target and there's still a left node, keep going
            return self.left.contains(target)

        # RIGHT
        else:
            # if there are no more right nodes, we hit a dead end and target isn't inside tree
            if not self.right:
                return False
            # if current node != target and there's still a right node, keep going
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):

        # check the whole right branch until we're at the last leaf
        if not self.right:
            # return node we're on, this is what ends the recursion
            return self.value
        else:
            # keep er goin
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        # fn is going to be the function we pass in
        # call the fn on the value at this node
        fn(self.value)

        # pass function to the left and right children
        # recursion stops if self.left/right is None
        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)


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

# # old version time complexity is O(n^c) methinks (would O(n^2) count?)
# NEW version
bst1 = BSTNode(names_1[0])
bst2 = BSTNode(names_2[0])

# fill in 2 bsts with a name list
for name in names_1:
    bst1.insert(name)
for name in names_2:
    bst2.insert(name)

test_name = "Hallie Vazquez"
print(bst1.contains(test_name) and bst2.contains(test_name))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
