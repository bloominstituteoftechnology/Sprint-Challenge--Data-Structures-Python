class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if root is not empty and value is greater than root, place value to right of root
        if (value >= self.value) and (self.right != None):
            self.right.insert(value)
        # if root is empty and value is greater than root, create a node and place value to right of root
        if (value >= self.value) and (self.right == None):
            new_node = BSTNode(value)
            self.right = new_node
        # if root is not empty and value is lesser than root, place value to right of root
        if (value < self.value) and (self.left != None):
            self.left.insert(value)
        # if root is empty and value is lesser than root, create a node and place value to left of root
        if (value < self.value) and (self.left == None):
            new_node = BSTNode(value)
            self.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if (target>self.value):
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        if (target<self.value):
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False