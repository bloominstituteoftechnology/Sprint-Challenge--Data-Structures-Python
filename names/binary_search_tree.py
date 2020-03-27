# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new value is less than the current node
        if value < self.value:
            # if there is no child on the left
            # this will become the leaf node
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # if the new value is greater than or equal to current node
        if value >= self.value:
            # if there is no child on the right
            # this will become the max
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                # else, follow the path right again
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value) #base case
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # # DAY 2 Project -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     if node.left:
    #         self.in_order_print(node.left)
    #     if node.right:
    #         # print the value, and move to the right children nodes
    #         # to preserve the sequence
    #         print(node.value)
    #         self.in_order_print(node.right)
    #     else:
    #         # if you've arrived at a leaf
    #         # print the value
    #         print(node.value)

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # create a queue
    #     q = Queue()
    #     # add root to queue
    #     q.enqueue(node)

    #     # as long as the queue isn't empty
    #     while q.len() > 0:
    #         # pop out the root and print its value
    #         current_node = q.dequeue()
    #         print(current_node.value)
    #         # check if it has any children nodes. if it does, enqueue them
    #         if current_node.left:
    #             q.enqueue(current_node.left)
    #         if current_node.right:
    #             q.enqueue(current_node.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # create a stack
    #     s = Stack()
    #     # add root to stack
    #     s.push(node)
    #     # as long as the stack isn't empty
    #     while s.len() > 0:
    #         # pop out the current node and print its value
    #         current_node = s.pop()
    #         print(current_node.value)
    #         # add any children nodes to the stack
    #         if current_node.left:
    #             s.push(current_node.left)
    #         if current_node.right:
    #             s.push(current_node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
