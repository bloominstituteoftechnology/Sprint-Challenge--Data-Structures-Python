#import sys
#sys.path.append('../queue_and_stack')
#from dll_queue import Queue
#from dll_stack import Stack
#from collection import deque

class BinarySearchTreeNode: # self is a circle/node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # base case: epmty parking spot to occupy
        # keep moving towards base case
        # self.left and/or self.right need to be valid nodes
        # for us to call 'insert' on them
        if value < self.value:
            #check if self.left is a valid node
            if self.left:
                self.left.insert(value)
                # the left side is empty
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTreeNode(value)
                # otherwise, value >= self.value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # apply the callback function to every node of our tree
    # at least O(n), could be worse depending on the callback
    def for_each(self, cb):
        cb(self.value)
        # base case: the node has no children
        # call the cb on the children of this node
        # lets check that this node has children
        if self.left:
            self.left.for_each(cb)
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
        queue.enqueue(self)
        while queue.size > 0:
            current_node = queue.dequeue()
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.size > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)

            print(current_node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

''' # lecture notes

    def depth_first_iterative_for_each(self, cb):
        stack = [] # will store the nodes
        # add the root of the tree to the stack
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check is left child exists
            if current_node(left):
                stack.append(current_node.left)
            cb(current_node.value)

# lecture notes
    def breadth_first_iterative_for_each(self, cb):
        # depth-first : Stack
        # breadth-first : queue
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left: # flip ordering, left to right here, breadth first
              q.append(current_node.left)
            if current_node.right:
              q.append(current_node.right)
            cb(current_node.value)
'''
