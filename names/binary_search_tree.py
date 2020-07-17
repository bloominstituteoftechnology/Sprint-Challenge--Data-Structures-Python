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
        
        if value < self.value:
            #If there is no child insert value here 
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: Self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: if target is less than self.value
        elif target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        #Case 3: otherwise 


    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        if not self.right:
            return self.value
        return self.right.get_max()

        #Iterative appraoch
        # max_value = self.value
        # current = self

        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        if self is None:
            return

        if self.left is not None:
            self.left.in_order_print()

        print(self.value)

        if self.right is not None:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     if self is None:
    #         return
    #     # Use a queue to form a "line"
    #     # for the nodes to "get in"
    #     queue = Queue()
    #     # start by placing the root in the queue if not None
    #     queue.enqueue(self)
    #     #need a while loop to iterate
    #     #while length of Q is greater than 0:

    #     while queue.__len__() > 0:
    #         #D-Q item in front of queue
    #         #print that item
    #         n = queue.dequeue()
    #         print(n.value)

    #         if 



        #place current items left node in Q if not None
        # place the current items right node in queue if not None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        #initialize an empty stack
        # push the root node onto the stack

        #need a while loop to manage our iteration
        # if stack is not empty enter the while loop 
            #print top item off the stack 
            #print that item's value

            #if there is a right subtree
                #push the right item onto the stack

            #if there is a left subtree 
                #push left item onto the stack

            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
