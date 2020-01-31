class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare to root node
        # If lesser go to left child
        if (value < self.value):
            if (self.left is None):
                # insert
                self.left = BinarySearchTree(value)
            else:
                # move left
                self.left.insert(value)
        # If greater or equal to, go right
        elif (value >= self.value):
            if (self.right is None):
                # insert
                self.right = BinarySearchTree(value)
            else:
                # move right and go through insert function
                self.right.insert(value)     

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If root is target, return
        if (target == self.value):
            return True
        elif (target < self.value):
            if (self.left is None):
                return False
            else:
                # move left
                # repeat
                return self.left.contains(target)
        elif (target > self.value):
            if (self.right is None):
                return False
            else:
                # move right
                # repeat
                return self.right.contains(target)