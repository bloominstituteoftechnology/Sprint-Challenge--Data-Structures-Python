

class BinarySearchTree:
    def __init__(self):
        self.root_node = None
        
    def isEmpty(self):
        return self.root_node is None
    
    def insert(self, value):
        if self.isEmpty():
            self.root_node = BSTNode(value)
        else:
            self.root_node.insert(value)
            
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
        
    #Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
                
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left else False
        else:
            return self.right.contains(target) if self.right else False