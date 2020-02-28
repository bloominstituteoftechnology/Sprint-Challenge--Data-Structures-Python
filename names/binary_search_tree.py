import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Value greater than tree value => go right
        if value >= self.value:
            # If no value to the right, create one
            if not self.right:
                self.right = BinarySearchTree(value)
            # Otherwise, move to that level recursively
            else:
                self.right.insert(value)
        # Value less than tree value => go left
        elif value < self.value:
            # If no value to the left, create one
            if not self.left:
                self.left = BinarySearchTree(value)
            # Otherwise, move to that level recursively
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If tree value is our value, we found it, so return True
        if self.value == target:
            return True
        # If tree value is less than our value, look right
        elif target > self.value:
            # If no value to the right,
            #  return False b/c tree doesn't contain our value
            if not self.right:
                return False
            # Otherwise, move to the next level recursively
            return self.right.contains(target)
        # If tree value is greater than our value, look left
        elif target < self.value:
            # If no value to the left,
            #  return False b/c tree doesn't contain our value
            if not self.left:
                return False
            # Otherwise, move to the next level recursively
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # If no nodes to the right, there are no values
        #  greater than the current value, so return
        if not self.right:
            return self.value
        # Otherwise, move right and recurse
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Run cb on current level
        cb(self.value)
        # Recurse left
        if self.left:
            self.left.for_each(cb)
        # Recurse right`
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        
        while queue.len():
            item = queue.dequeue()
            print(item.value)
            if item.left:
                queue.enqueue(item.left)
            if item.right:
                queue.enqueue(item.right)
    

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len():
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
