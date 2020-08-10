class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
            
        if self.value >= target:
            if self.right is None:
                return False
            else:
                return self.right.contain(target)
        
        if self.value < target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)