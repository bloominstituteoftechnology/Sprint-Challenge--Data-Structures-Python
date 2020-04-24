from collections import deque

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left &| self.right have to be valid nodes to call insert
        if value < self.value:
            # check left validity
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            # check right validity
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
        else:
            return False        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def depth_first_iterative_for_each(self, cb):
        stack = []
        stack.append(self)
        # loop while the stack has elements
        while len(stack) > 0:
            cur_node = stack.pop()
            # check if right exists
            if cur_node.right:
                stack.append(cur_node.right)
            # check if left exists
            if cur_node.left:
                stack.append(cur_node.left)
            cb(cur_node.value)

    def breadth_first_iterative_for_each(self, cb):
        q = deque()
        q.append(self)

        while len(q) > 0:
            cur_node = q.popleft()
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            cb(cur_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            if node.left:
                self.in_order_print(node.left)
            print(node.value)
            if node.right:
                self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()
        q.append(self)

        while len(q) > 0:
            cur_node = q.popleft()
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            print(cur_node.value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            cur_node = stack.pop()
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
            print(cur_node.value)
