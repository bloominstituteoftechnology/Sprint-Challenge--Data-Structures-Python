# import sys
# sys.path.append('../queue_and_stack')
from queue import Queue
from stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Empty tree
        if self.value == None:
            self.value = value
            return

        if value < self.value:
            if self.left == None:
                # End of the tree. Add a new node.
                self.left = BinarySearchTree(value)
            else:
                # Navigate left recursively
                self.left.insert(value)
            return

        if value >= self.value:  # This tree allows duplicates
            if self.right == None:
                # End of the tree. Add a new node.
                self.right = BinarySearchTree(value)
            else:
                # Navigate right recursively
                self.right.insert(value)
            return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == None:
            # Empty list
            return False

        if self.value == target:
            # Found it
            return True

        if target < self.value:
            if self.left == None:
                # Max depth of the tree
                return False
            else:
                # Navigate left recursively
                return self.left.contains(target)

        if target > self.value:
            if self.right == None:
                # Max depth of the tree
                return False
            else:
                # Navigate left recursively
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right != None:
            self = self.right

        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # Parse depth-first, in-order (LNR)

        # Go Left
        if self.left != None:
            self.left.for_each(cb)

        # Run callback function on this node
        cb(self.value)

        # Go Right
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # In-order traversal
        # L N R

        # def cb(x): print(x)
        # self.for_each(cb)

        # Go Left
        if self.left != None:
            self.left.in_order_print(self.left)

        # Print this node between left and right traversals
        print(self.value)

        # Go Right
        if self.right != None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        parse_order = Queue()
        parse_order.enqueue(self)

        while parse_order.len() > 0:
            current_node = parse_order.dequeue()
            if current_node.left:
                parse_order.enqueue(current_node.left)
            if current_node.right:
                parse_order.enqueue(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # In-order traversal
        # L N R

        self.pre_order_dft(node)
        # TODO: Switch to iterative function?

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # N L R

        # Print this node first
        print(self.value)

        # Go Left
        if self.left != None:
            self.left.pre_order_dft(self.left)

        # Go Right
        if self.right != None:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # L R N

        # Go Left
        if self.left != None:
            self.left.post_order_dft(self.left)

        # Go Right
        if self.right != None:
            self.right.post_order_dft(self.right)

        # Print this node last
        print(self.value)


# Testing
apple = BinarySearchTree(1)
apple.insert(8)
apple.insert(5)
apple.insert(7)
apple.insert(6)
apple.insert(3)
apple.insert(4)
apple.insert(2)
