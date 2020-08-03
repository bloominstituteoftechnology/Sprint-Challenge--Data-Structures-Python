class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
            
        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
