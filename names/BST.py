class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if value is greater than node, look left 
        if value < self.value: #we'll think of value as number
            # if something (value) is already there
            if self.left:
                #move to the left
                self.left.insert(value)
                #if there is no value there, make a new value by calling the BST
            else:
                self.left = BinarySearchTree(value)
                
        #if value is greater than or equal to root node, then move right
        if value >= self.value:
            #if something is already there 
            if self.right:
                #move to the right 
                self.right.insert(value)
            else:
                #if there is no value...make a new value by calling BST 
                self.right = BinarySearchTree(value)
                
    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        #if value is less than target value, move left?
        if target < self.value:
            if self.left:
                #if there is 
                return self.left.contains(target)
            else:
                #if there's nothing to the left 
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        #if there is nothing on the right
        if not self.right:
            #return value b/c this must be the biggest node 
            return self.value
        else:
            #if not call this function on the node to the right...makes sense
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #first call cb on self.value
        cb(self.value)
        #if left 
        if self.left:
            #call it 
            self.left.for_each(cb)
            #if right 
        if self.right:
            self.right.for_each(cb)