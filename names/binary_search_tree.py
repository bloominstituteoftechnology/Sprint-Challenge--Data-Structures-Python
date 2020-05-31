class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # each node is a tree
    def insert(self, value):
        # nothing in the tree must add something, start on insert
        # if inserting we must already have a tree/root
        # if value is less than self.value go left, make a new tree/node if empth,
        # otherwise keep going(recursion)
        # if greater than or equal to
        # if root is none set root to node
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # recurse to the left
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                # recurse to the right

            else:
                self.right.insert(value)

        # pre follow along
        # if self.value == None:
        #     self.value = value
        #     return self.value
        # if self.value < value:

        #     if self.right is None:
        #         self.right = BinarySearchTree(value)
        #     else:
        #         return self.right.insert(value)
        # else:
        #     if self.left is None:
        #         self.left = BinarySearchTree(value)
        #     else:
        #         return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target == self.value, return it
        # else go left or right if smaller or bigger
        # base case
        if target == self.value:
            return True
            # if target is less than self.value we go left
        if target < self.value:
            if self.left is None:
                return False
            else:
                # recurse
                self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
                # return the recursion or you will lose state

        # pre follow
        #         # if target == self.value:
        #     return True
        # elif target < self.value and self.left is None:
        #     return False
        # elif target >= self.value and self.right is None:
        #     return False
        # elif target < self.value and self.left is not None:
        #     return self.left.contains(target)
        # elif target >= self.value and self.right is not None:
        #     return self.right.contains(target)

    # Return the maximum value found in the tree
    # if right exists, go right, else return self.value
    # if self.right is none you keep going right, then recurse
    # what structure describes a recursive function, answer: a call stack d
    # dft = depth first traversal
    # depth search Go left until you can't, then go right. When both are dead ends, go up until the next unexplored path and repeat
    # add it to the stack
    # breadth first traversal bft
    # search done when you find what you are looking for
    # traversal go through the entire tree
    # while stack not empty loops are used
    # if left
    #   add left to stack
    # if right
    #   add right to stack
    # in a search if target == value then return
    # recursion is creating a stack

    # BFT
    # make a queue
    # put root in the queue
    # while queue is not empty
    # pop out front of queue
    # do the thing CB?
    # if left:
    #   add to to the back of queue
    # if right:
    #   add right to the back of the queue
    # can change from a stack or queue

    # steps:   first things first
    # make a stack
    # put root into stack
    # take out root(pop) and check left, if left add left to stack
    # if right add right to stack

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call the callback function first on self.value
        cb(self.value)
        # look for other nodes if they exist recurse
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

        # stack = Stack()
        # # root node
        # stack.push(self)
        # while there is something in the stack stack.len > 0

        # while stack.len() > 0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # specific vocab term, at work a colleague want's you to use an in order print
    # in order print left, root(print),  right
    # node recursion policy, go left, go left etc... on return print then go right
    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    # def bft_print(self, node):
    #     # make a queue
    #     queue = Queue()
    #     queue.enqueue(self)

    #     while queue.len() > 0:
    #         node = queue.dequeue()
    #         print(node.value)
    #         if node.left:
    #             queue.enqueue(node.left)
    #         if node.right:
    #             queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    # def dft_print(self, node):
    #     # make a stackey
    #     stack = Stack()
    #     stack.push(self)
    #     while stack.len() > 0:
    #         node = stack.pop()
    #         print(node.value)
    #         if node.left:
    #             stack.push(node.left)
    #         if node.right:
    #             stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass