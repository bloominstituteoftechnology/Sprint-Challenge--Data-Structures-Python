class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new nodes value is less than the current nodes value    
        if value < self.value:
            # if there is no left child already here
            if not self.left:
                # add the new node to the left
                # create a BSTNode and encapsulate the value in it then set it to the left
                self.left = BSTNode(value)
            else:
                # otherwise call insert on the left node
                return self.left.insert(value)
        # otherwise (the new nodes value is greaterthan or equal to the current node value)
        if value >= self.value:
            # if there is no right child already here
            if not self.right:
                # add the new node to the right
                # create a BSTNode and encapsulate the value in it then set it to the right
                self.right = BSTNode(value)
            else:
                # otherwise call insert on the right node
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
        if target == self.value:
            # return True
            return True
        # check if the target is less than the current nodes value
        elif target < self.value:
            # if there is no left child already here
            if not self.left:
                # return False
                return False
            else:
                # return a call of contains on the left child passing in the target value
                return self.left.contains(target)
        # otherwise (the target is greater than the current nodes value)
        elif target > self.value:
            # if there is no right child already here
            if not self.right:
                # return False
                return False
            else:
                # return a call of contains on the right child passing in the target value
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check for an empty tree
        if self.right is None and self.left is None:
            # return None
            return None
        
        # check if there is no node to the right
        if not self.right:
            # return the nodes value
            return self.value
        else:
            # return a call to get max on the right child
            return self.right.get_max()

    def for_each(self, fn):
        # call the function passing in the current nodes value
        fn(self.value)
        
        # if there is a node to the left
        if self.left:
             # call the function on the left value
            self.left.for_each(fn)
        # if there is a node to the right
        if self.right:
            # call the function on the right node
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft() 