from queue import Queue


"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        val_node = BSTNode(value)
        if value >= self.value:
            if self.right is None:
                self.right = val_node
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = val_node
            else:
                self.left.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
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
        if not self.right:    
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        

#     # Part 2 -----------------------
    
#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
#     def in_order_print(self):
#         if self.left:
#             self.left.in_order_print()
#         print(self.value)
#         if self.right:
#             self.right.in_order_print()

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
#     # Queue
#     def bft_print(self):
#         # Create a queue
#         queue = Queue()
#         # Add node to queue
#         queue.enqueue(self)
#         # Check if length of queue is greater than sero
#         while queue.storage.length() > 0:
#             # pop the cur_node off the stack
#             cur_node = queue.dequeue()
#             # print the current node value
#             print(cur_node.value)
#              # check to see if there is a left node
#             if cur_node.left:
#                 # enqueue the left node
#                 queue.enqueue(cur_node.left)
#             # check to see if there is a right node
#             if cur_node.right:
#                 # enqueue the right node
#                 queue.enqueue(cur_node.right)
            
            
        

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     # Stack
#     def dft_print(self):
#        # Instantiate new stack
#         stack = Stack()
#         stack.push(self)
#         while stack.storage.length() > 0:
#             cur_node = stack.pop()
#             print(cur_node.value)
#             if cur_node.left:
#                 stack.push(cur_node.left)
#             if cur_node.right:
#                 stack.push(cur_node.right)
            
                        
#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self):
#         print(self.value)
#         if self.left:
#             self.left.pre_order_dft()
#         if self.right:
#             self.right.pre_order_dft()

#     # Print Post-order recursive DFT
#     def post_order_dft(self):
#         if self.left:
#             self.left.post_order_dft()
#         if self.right:
#             self.right.post_order_dft()
#         print(self.value)   
        
        

# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_dft()  
