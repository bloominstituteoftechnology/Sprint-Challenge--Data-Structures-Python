

class BinarySearchTree:
    def __init__(self):
        self.root_node = None
        
    def isEmpty(self):
        return self.root_node is None
    
    def insert(self, value):
        if self.isEmpty():
            self.root_node = BSTNode(value)
        else:
            self.root_node = insert(value)
            
    def contains(self, target):
        if self.isEmpty():
            return False
        else:
            return self.root_node.contains(target)
        
        
# BSTNode class

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        