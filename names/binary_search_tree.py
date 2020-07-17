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
        # Case 1: value is less than self.value
        if value < self.value:
            if self.left is None:
                # create new node
                self.left = BSTNode(value)
            else:
                # Repeat the process on the left subtree (recursion)
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat the process on the right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target 
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # pass
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # pass
        fn(self.value)
        # Case 1
        if self.left:
            self.left.for_each(fn)
        
        # Case 2:
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass
         
        if self.value is None:
            return
        if self.left:
            self.left.in_order_print(node)
        # print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
