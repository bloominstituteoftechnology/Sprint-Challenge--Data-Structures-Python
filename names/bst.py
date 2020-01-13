class BSTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTree(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = BSTree(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        # go right if value is less than target
        if self.value < target:
            if self.right:
                return self.right.contains(target)
        # go left if value is greater than target
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
        else:
            return False