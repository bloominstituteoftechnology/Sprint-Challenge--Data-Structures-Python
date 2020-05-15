from collections import deque
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
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.length = 0
    def __len__(self):
        return f'{self.length}'
    # Insert the given value into the tree
    def insert(self, value):
        self.length += 1
        # value is less than 
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else: #value is greater than or equal to
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # target is less than node value
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else: #value is greater than or equal to
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
    
    # Return the maximum value found in the tree
    def get_max(self):
        #self 
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # calls the callback on the value
        fn(self.value)
        #checks for left node
        if self.left:
            self.left.for_each(fn)
        #checks for right node
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #DFS search 
        # node = root of tree
        if not node:
            return
        else:
            # traverse left subtree
            self.in_order_print(node.left)
            # print visited node
            print(node.value)
            # traverse right subtree
            self.in_order_print(node.right)
           

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #FIFO ordering
        queue = deque()
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
        #FILO ordering
        stack = []
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            # print visited node
            print(node.value)
            # traverse left subtree
            self.pre_order_dft(node.left)
            # traverse right subtree
            self.pre_order_dft(node.right)
        else: 
            return

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            # traverse left subtree
            self.post_order_dft(node.left)
            # traverse right subtree
            self.post_order_dft(node.right)
            # print visited node
            print(node.value)
        else: 
            return


# bts = BinarySearchTree(7)
# bts.insert(2)
# bts.insert(3)
# bts.insert(4)

# bts.in_order_print(bts)
# print('---------------')
# # bts.dft_print(bts)
# # bts.bft_print(bts)
# bts.pre_order_dft(bts)
