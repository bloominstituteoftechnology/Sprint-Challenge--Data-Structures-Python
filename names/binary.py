

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if self.value <= value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            return self.left.contains(target)

        if self.value < target:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        return self.value

        # else:
        #     curr = self.right
        #     while curr:
        #         curr = curr.right
        #         return curr.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # print_curr_node = lambda x: print(f'current node is {x}')
    # n = BSTNode(9)
    # n.insert(7)
    # n.insert(10)
    # n.for_each(print_curr_node) // returns all node values

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def traverse(self, fn):
        if self.left:
            self.left.traverse(fn)
        fn(self.value)

        if self.right:
            self.right.traverse(fn)

    def in_order_print(self, node):
        def print_node(x): return print(x)
        node.traverse(print_node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def breadth(self, fn):
        fn(self.value)

    def bft_print(self, node):
        # add the first node to queue
        # while queue is not empty
        # remove first node from queue
        # print removed node
        # add left and right into the queue
        queue = []
        queue.append(node)
        while len(queue) > 0:
            print(queue[0].value)
            if queue[0].left is not None:
                queue.append(queue[0].left)
            if queue[0].right is not None:
                queue.append(queue[0].right)
            queue.pop(0)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = []
        stack.append(node)
        curr_node = node
        while len(stack) > 0:
            # switch to 0 for breadth first
            curr_node = stack.pop(len(stack)-1)
            if curr_node.right is not None:
                stack.append(curr_node.right)

            if curr_node.left is not None:
                stack.append(curr_node.left)

            print(curr_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


def print_curr_node(x): return print(f'current node is {x}')
