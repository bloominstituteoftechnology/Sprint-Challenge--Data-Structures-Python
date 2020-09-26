class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BST(value)
        if self.value is None:
            self.value = value
            return
        
        elif value < self.value:
            if self.left is None:
             self.left = node
            else:
             self.left.insert(value)
        
        
        elif value >= self.value:
            if self.right is None:
             self.right = node
            else:
             self.right.insert(value) 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
       
        if target == self.value:
            return True
        
        elif target < self.value and self.left:
            return self.left.contains(target)
        
        elif target > self.value and self.right:
            return self.right.contains(target)
     
        else:
            return False