"""Implement a Binary Search Tree"""

class BinarySearchTree:
    """Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Insert the given value into the tree"""
        # insert left side
        if value < self.value:
            # there isn't a self.left for this node
            if not self.left:
                # insert into self.left
                self.left = BinarySearchTree(value)
            else:
                # there is a self.left, recurse to the left
                self.left.insert(value)
        # insert right side
        else:
            # there isn't a self.right for the current node
            if not self.right:
                # insert into self.right
                self.right = BinarySearchTree(value)
            else:
                # there is a self.right, recurse to the right
                self.right.insert(value)

    def contains(self, target):
        """Return True if the tree contains the value
        False if it does not"""

        # base case
        if target == self.value:
            return True

        # if target is smaller go left
        if target < self.value:

            # if nowhere else to go
            if not self.left:
                return False

            # recurse left side
            else:
                return self.left.contains(target)

        # if target is bigger go right
        elif target > self.value:

            # if nowhere else to go
            if not self.right:
                return False

            # recurse right side
            else:
                return self.right.contains(target)

    def get_max(self):
        """Return the maximum value found in the tree"""
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        """Call the function `cb` on the value of each node
        You may use a recursive or iterative approach"""
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    def in_order_print(self, node):
        """Print all the values in order from low to high
        Hint:  Use a recursive, depth first traversal"""
        # if left node
        if node.left:
            # recurse down the left side
            node.in_order_print(node.left)

        # print left side then root then right side
        print(node.value)

        # if right node
        if node.right:
            # recurse down the right side
            node.in_order_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    def pre_order_dft(self, node):
        """Print Pre-order recursive DFT"""
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)


    def post_order_dft(self, node):
        """Print Post-order recursive DFT"""
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)
