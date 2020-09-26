class BSTNode:
    def __init__(self, value):
        # Value is supposed to be an int/float
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #Start from our reference point, our main/current node
        curr_node = BSTNode(self.value)
        #Move through the nodes from top to bottom to find place for new node
        #New nodes are always inserted at bottom of tree (as a leaf)
        while curr_node:
            #If the new value is less than the current node's value
            if value < self.value:
                #If the left node is empty
                if self.left is None:
                    #Our new node becomes the left node
                    self.left = BSTNode(value)
                    return
                #If there is already a left node, we relocate to that left node
                else:
                    curr_node = curr_node.left
            #If the new value is greater than or equal to the current node's value
            else:
                #If the right node is empty
                if self.right is None:
                    #Our new node becomes the right node
                    self.right = BSTNode(value)
                    return
                #Otherwise, we relocate to the right node
                else:
                    #Relocate to right node
                    curr_node = curr_node.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        #If we've found the target value
        if target == self.value:
            return True
        
        #If we need to move left because the target is less than our current node
        elif target < self.value:
            #and we can move left
            if self.left:
                #move left and start from base cases
                self.left.contains(target)
            else:
                return False
        #If we need to move right because the target is greater than our current node
        else:
            #and we can move right
            if self.right:
                self.right.contains(target)
                #move right and start from base cases
            else:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        #Move right down BST until we can't anymore
        #That's the max!

        #current max starts as main node's value
        curr_max = self.value
        #BASE CASE: if we can't move right, return current max
        if not self.right:
            return curr_max
        #RECURSIVE CASE: if we can move right, we do so and adjust the current max
        else:
            return self.right.get_max()




    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        #BASE CASE: no children, so do nothing

        #RECURSIVE CASE: one or more children
        #this operation will move from left to right before moving deeper
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        #BASE CASE: the node is null (do nothing)
        #Visit the left subtree
        if self.left:
            self.left.in_order_print()
        #Visit the root and print it
        print(self.value)
        #Visist the right subtree
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        #Create a stack to keep trak of nodes we are processing
        #push self into stack
        stack = []
        stack.append(self)

        #while something still in the stack
        #(whiel we are not done processing all nodes)
        while len(stack) > 0:
            #pop the node off the top of the stack
            node = stack.pop()
            #print the node's value
            print(node.value)
            #push its left and right cchildren onto the stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass