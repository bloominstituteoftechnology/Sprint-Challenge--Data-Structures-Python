class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
            # if value < Node's value, we need to go left
        if value < self.value:
            # if we see that there is no left child
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            else:
                # call the left child's insert method
                self.left.insert(value)
        # if value >= Node's value, we need to go right
        else:
            # we need to go right if we see there is no right child
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
                # otherwise if there is a child
            else:
                # call the right child's insert method
                self.right.insert(value)

    def contains(self, target):
        # if the value of the node matches the value of the target, we found what we're looking for
        if target == self.value:
            return True

        # compare the target against this node's value to determine which direction to go in
        if target < self.value and self.left:
            return self.left.contains(target)

        # if the value isn't on the left, then we check to see if we can go right
        if self.right:
            return self.right.contains(target)

        # if both conditions fail, then we value isn't in the tree
        return False