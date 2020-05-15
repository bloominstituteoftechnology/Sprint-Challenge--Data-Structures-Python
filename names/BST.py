class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            self.left.in_order_print(node.left)
        print(self.value)
        if node.right is not None:
            self.right.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    from collections import deque

    def bft_print(self, node):
        queue = self.deque()

        queue.append(node)
        while len(queue) > 0:
            current = queue.popleft()
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            

        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [] 
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        stack = [] 
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        stack = [] 
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            print(current.value)