class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)