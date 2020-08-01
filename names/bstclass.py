class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Is the value less than the current node's value?
        if value < self.value:
            # insert to the left
            if self.left == None:
                # No "left" child, insert the new node here
                self.left = BSTNode(value)
            else:
                # a "left" child exists, invoke the the child's insert method
                self.left.insert(value)
            
            return

        # Is the value greater than the current node's value?
        if value > self.value:
            # insert to the right
            if self.right == None:
                # No "right" child, insert the new node here
                self.right = BSTNode(value)
            else: 
                # a "right" child exists, invoke the the child's insert method
                self.right.insert(value)

            return

        # Is the value equal to the current node's value?
        if value == self.value:
            # Already have this value.. nothing to do.  Return
            return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Is this the target node?
        if self.value == target:
            return True

        # Not the target node, is the target less than the current node?
        if target < self.value:
            # Are there any "left" nodes to search?
            if self.left == None:
                # No more nodes to search -> the target is not found
                return False

            # A left node or sub-tree exists, return an invocation
            #   of the contains method on the left child node
            return self.left.contains(target)

        # Not the target node, is the target greater than the current node?
        if target > self.value:
            # Are there any "right" nodes to search?
            if self.right == None:
                # No more nodes to search -> the target is not found
                return False

            # A right node or sub-tree exists, return an invocation
            #   of the contains method on the right child node
            return self.right.contains(target)
