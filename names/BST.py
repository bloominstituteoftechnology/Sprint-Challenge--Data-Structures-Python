class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = BSTNode(value)
        # if value is less than current, move left
        elif value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # if value is more than or equal to current, move right
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the target entered is the the root, return True
        if target == self.value:
            return True
        # save the target to be updated in a loop
        curr_value = target
        # keep track of current iteration of nodes
        current_node = self
        while current_node != None:
            # if its the current number, return True
            if current_node.value == curr_value:
                return True
            # if its less than, move left
            elif curr_value < current_node.value:
                current_node = current_node.left
            # if its equal to or greater than, move right
            elif curr_value >= current_node.value:
                current_node = current_node.right
            # if its None, return False
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if root is the only node, return value
        if self.right == None:
            return self.value

        # hold value
        max_value = self.value
        current_node = self
        # loop as long as theres a node to the right
        while current_node != None:
            max_value = current_node.value
            current_node = current_node.right

        # return max_value
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # 1. Base case - no more nodes in our subtree
        # 2. Recursive case
        fn(self.value)

        if self.left is not None:  # if self.left
            self.left.for_each(fn)
        if self.right is not None:  # if self.right
            self.right.for_each(fn)