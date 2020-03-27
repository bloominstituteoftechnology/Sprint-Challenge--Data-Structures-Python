class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None     

    # Insert the given value into the tree
    def insert(self, newValue):
        if newValue < self.value:
            if self.left:
                self.left.insert(newValue)
            else:
                self.left = BinarySearchTree(newValue)
        else:
            if self.right:
                self.right.insert(newValue)
            else:
                self.right = BinarySearchTree(newValue)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)