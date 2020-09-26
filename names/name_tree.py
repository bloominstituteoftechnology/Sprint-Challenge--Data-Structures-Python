class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        if self.left and self.right:
            return(f"Node: {self.value}, Left: {Self.right}, Right: {self.right}")
        elif self.left is not None and self.right is None:
            return(f"Node: {self.value}, Left: {self.left}, Right: None")
        elif self.left is None and self.right is not None:
            return(f"Node: {self.value}, Left: None, Right: {self.right}")
            
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
                
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False
                