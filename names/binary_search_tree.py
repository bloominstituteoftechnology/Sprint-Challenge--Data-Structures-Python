
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

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


