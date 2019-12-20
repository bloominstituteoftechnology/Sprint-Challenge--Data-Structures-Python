# import sys
# from dll_queue import Queue
# from dll_stack import Stack

# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting, there must be a root
        # if value is < self.value
        if value < self.value:
            # if not keep going
            if self.left is None:
                self.left = BinarySearchTree(value)
            # make a left node
            else:
                self.left.insert(value)
        # if >= then go right and
        elif value >= self.value:
            # if not keep going
            if self.right is None:
                self.right = BinarySearchTree(value)
            # make a new node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target = self.value. return
        # If not, go left or right depending on value size
        if self.value == target:
            return True
        if self.value < target:
            if self.right:
                return self.right.contains(target)
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists go right
        # otherwise return self.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # counting first value
        cb(self.value)
        # counting left side
        if self.left:
            self.left.for_each(cb)
        # counting right side
        if self.right:
            self.right.for_each(cb)




