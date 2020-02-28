# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target >= self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
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
        if self.right and self.left:
            cb(self.value)
            self.right.for_each(cb) 
            self.left.for_each(cb)
        elif self.left:
            cb(self.value)
            self.left.for_each(cb)
        elif self.right:
            cb(self.value)
            self.right.for_each(cb)
        else:
            cb(self.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return

        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     queue = Queue()
    #     temp_node = None

    #     queue.enqueue(node)

    #     while queue.len() > 0:
    #         temp_node = queue.dequeue()
    #         print(temp_node.value)
            
    #         if temp_node.right:
    #             queue.enqueue(temp_node.right)
            
    #         if temp_node.left:
    #             queue.enqueue(temp_node.left)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # initialize a stack
    #     stack = Stack()
    #     temp_node = None
    #     # push root to stack
    #     stack.push(node)
    #     # while stack not empty
    #     while stack.len() > 0:
    #     # pop top item out of stack into temp
    #         temp_node = stack.pop()
    #     # DO THE THING!!!!!!
    #         print(temp_node.value)
    #     # if temp has right right put into stack
    #         if temp_node.right:
    #             stack.push(temp_node.right)
    #     # if temp has left left put into stack
    #         if temp_node.left:
    #             stack.push(temp_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if not node:
            return

        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if not node:
            return

        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)
