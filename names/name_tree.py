
class NameTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # need to instert values

        # Insert the given value into the tree
    def insert(self, value):
        # lower values to left
        if value < self.value:
            if self.left is None:
                self.left = NameTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = NameTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left != None:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right != None:
                return self.right.contains(target)
            else:
                return False
