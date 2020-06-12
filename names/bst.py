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
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # value == target
        if self.value == target:
            return True
        # value != target
        else:
            # is the target lower than the value?
            if target < self.value:
                # is there any child node?
                if not self.left:
                    return False
                # is the left child node our target?
                if self.left.value == target:
                    return True
                else:
                    self.left.contains(target)
            else: # target >= self.value
                # is there any child node?
                if not self.right:
                    return False
                # is the right child node our target?
                if self.right.value == target:
                    return True
                else:
                    self.right.contains(target)