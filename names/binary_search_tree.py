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


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        storage = self.storage
        return storage.append(value)

    def pop(self):
        storage = self.storage
        if len(storage) > 0:
            return storage.pop()
        else:
            return None


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
                return "added"
            # ELSE
            else:
                # Repeat the process on left subtree
                return self.left.insert(value)

        # Case 2: valuse is greater than or equal to self.value
        elif value > self.value:
            # If there is no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
                return "added"
            # ELSE
            else:
                # Repeat the process on left subtree
                return self.right.insert(value)
        # duplicates are okay and they go to the right

        #
        elif value == self.value:
            return "duplicate"

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
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
        # forget about the left subtree
        # iterate through the nodes using a loop construct

        # check to see if self.right exists, if not return the head
        if self.right is None:
            return self.value
        else:
            if self.right:
                # call get_max on current node
                return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive solution
        fn(self.value)
        # if self.right exists then call for_each on it
        if self.right:
            self.right.for_each(fn)
        # same for left
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return None

        # check if we can move left
        if self.left is not None:
            self.left.in_order_print(node)

        # visit the node by printing its value
        print(self.value)

        # check if we can move right
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # use a queue to form a "line"
        # for the nodes to "get in"

        # start by placing the root in the queue
        queue = Queue()
        queue.enqueue(node)
        # need a while loop to iterate
        # what are we checking in the while statement?
        #while length of queue is greater than 0
        while queue.__len__() > 0:
            temp = queue.storage[0]
            # place current item's left node in queue if not None
            if temp.left:
                queue.enqueue(temp.left)
            # place current item's right node in queue if not None
            if temp.right:
                queue.enqueue(temp.right)
            # dequeue item from front of queue
            queue.dequeue()
            #print that item
            print(temp.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        # initialize an empty stack
        stack = Stack()
        # push the root node onto the stack
        if node:
            stack.push(node)
        # need a while loop to manage our iteration
        # if stack is not empty enter the while loop
        while stack.__len__() > 0:
            temp = stack.storage[-1]
            # pop top item off the stack
            stack.pop()
            # if there is a right subtree
            # push right item onto the stack
            if temp.right:
                stack.push(temp.right)
        # if there is a left subtree
        # push left item onto the stack
            if temp.left:
                stack.push(temp.left)
        # print that item's value
            print(temp.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
