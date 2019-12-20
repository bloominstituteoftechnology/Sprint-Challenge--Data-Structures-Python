
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None  # left_LESS_subtree
        self.right = None  # right_GREATER_EQUAL_subtree

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = BinarySearchTree(value)
        else:
            if self.value > value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif self.value <= value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        else:
            if self.value > target:
                if not self.left or self.left.value is None:
                    return False
                elif self.left.value == target:
                    return True
                else:
                    return self.left.contains(target)
            elif self.value < target:
                if not self.right or self.right.value is None:
                    return False
                elif self.right.value == target:
                    return True
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
