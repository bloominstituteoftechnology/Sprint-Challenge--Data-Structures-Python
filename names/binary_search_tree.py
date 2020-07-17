class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left is None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value >= self.value:
            if not self.right is None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            if self.left is None:
                return False
            else:

                return self.left.contains(target)