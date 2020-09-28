class BSTNode:
    # initialize default values
    # self.value => value of the node
    # self.left & ".right => points to left and right nodes
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # insert a node to the tree
    def insert(self, value):
        # if the passed in node's value is less than the 
        # value of the node on the left...
        if value < self.value:
            # check if there is a node on the left.
            # if there is not, create a new tree and place
            # the new node on the left
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # else if the value of the new node is
        # greater than or equal to the current value...
        elif value >= self.value:
            # and there is no node on the right
            # create a new tree and place the new node 
            # on the right side of that tree
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    
    # find out if a node is in the tree
    def contains(self, target):
        # if the value of this node is the target node
        # return true
        if self.value == target:
            return True
        # if the target is less than the currnet nodes value...
        if target < self.value:
            # and there is no node on the left
            # return false
            # otherwise call our function again
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        # if the target is more than the current nodes value...
        else:
            # and there is no node on the right
            # return false
            # otherwise call our function again
            if not self.right:
                return False
            else:
                return self.right.contains(target)