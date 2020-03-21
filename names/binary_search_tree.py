class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):    
        if value >= self.value:
            if self.right==None:
                self.right=BinarySearchTree(value) 
            else:
                return self.right.insert(value)
        elif value<self.value:
            if self.left==None:            
                self.left=BinarySearchTree(value)
            else:
                return self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target==self.value:
            return True
        elif target>self.value:
            if self.right!=None:
                return self.right.contains(target)
        elif target<self.value:
            if self.left!=None:
                return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right==None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)