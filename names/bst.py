class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert here
            if self.left is None:
                self.left = BSTNode(value)
            # Else:
            else:
                # repeat the proces on left subtree
                self.left.insert(value)
            
        # Case 2: value is greater than self.value
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # Case 3; if value has duplicates       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Case 1: self.value is equal to the target
        if self.value == target:
            return True
        #Case 2 : target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        #Case 3:  otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)