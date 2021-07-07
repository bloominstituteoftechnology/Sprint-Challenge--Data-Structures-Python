class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #self will be the root
        # compare the target against self
        if target == self.value:
            return True
        if target < self.value:
        # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
        # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        
        while self.right is not None:
            current_max = self.right.value
            self.right = self.right.right
        return current_max
        
        # if not self.right:
        #     return self.value
        # return self.right,get_max()

    # Call the function `fn` on the value of each node
    # doesn't actually return anything
    def for_each(self, fn):
    # this method specifically does want to traverse every tree node
    # has to call the fn on self.value
        fn(self.value)
    # is there a left child?
        # if yes, call it's for_each with the same fn
        if self.left:
            self.left.for_each(fn)
    # is there a left child?    
        if self.right:
        # if yes, call it's for_each with the same fn            
            self.right.for_each(fn)