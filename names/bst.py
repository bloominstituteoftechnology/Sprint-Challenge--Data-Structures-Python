class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"<Value: {self.value}. Left: {self.left}. Right: {self.right}>"

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
        elif value < self.value and self.left is not None:
            self.left.insert(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)
        # < go left
        # >= go right

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left is None:
            return False
        elif target >= self.value and self.right is None:
            return False
        elif target < self.value and self.left is not None:
            self = self.left
            return self.contains(target)
        elif target >= self.value and self.right is not None:
            self = self.right
            return self.contains(target)
