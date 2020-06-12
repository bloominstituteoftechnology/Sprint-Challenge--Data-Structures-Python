class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
      
    def contains(self, target):
        if self is None:
            return False
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False