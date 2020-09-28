class BSTNode:
    """
    The left subtree of a node contains only nodes with values lesser than the node's values
    The right subtree of a node contains only nodes with values greater or equal to than the node's values
    The left and right subtree each must also be a binary search tree.
    """
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
        if self.value == target:
            return True
        elif self.value > target:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

# Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        current_node = self
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.right
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
