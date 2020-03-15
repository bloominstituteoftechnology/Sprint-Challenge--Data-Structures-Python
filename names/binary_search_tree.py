import sys
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
       # print(self.value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            else:
                self = self.right
                return self.insert(value)
        else:
            value < self.value
            if self.left is None:
                self.left = BinarySearchTree(value)
                return
            else:
                self = self.left
                return self.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return(True)

        elif target > self.value:
            if self.right is None:
                return False
            else:
                self = self.right
                return self.contains(target) 
        else:    
            if self.left is None:
                return False
            else:
                self = self.left
                return self.contains(target)        
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            self = self.right
            return self.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        # if self.right and self.left:
        #     self.left.for_each(cb)
        #     self.right.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
            

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
        stack = Stack()
        stack.push(node)
        while stack.len() != 0:
            look = stack.dll.head.value
            print(look)

            if look.right:
                stack.push(look.right)
            if look.left:
                stack.push(look.left)

            print(look.value)
            stack.pop(look)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [node]

        while stack != []:
 
            look = stack[-1]
            print(look.value)
            stack = stack[0:-1]
            if look.right is not None:
                stack.append(look.right)
                
            if look.left is not None:
                stack.append(look.left)

            
            

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value),
            

            node.pre_order_dft(node.left)

            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)

# a = BinarySearchTree(5)

# a.insert(6)

# a.insert(7)

# a.insert(-6)

# a.insert(-7)


# a.insert(-8)
# a.insert(10)
# a.insert(12)
# a.insert(13)
# a.insert(11)
# a.insert(14)
# a.insert(15)
# a.insert(19)
# a.insert(18)
# a.insert(17)



# arr = []
# cb = lambda x: arr.append(x)
# a.for_each(cb)
# #print(a.in_order_print(a))
# a.bft_print(a)

# a = BinarySearchTree(1)
# a.insert(8)
# a.insert(5)
# a.insert(7)
# a.insert(6)
# a.insert(3)
# a.insert(4)
# a.insert(2)

# a.pre_order_dft(a)
