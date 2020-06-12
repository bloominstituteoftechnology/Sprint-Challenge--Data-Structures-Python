class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        newNode = BSTNode(value)
        if self.value <= newNode.value:
            if self.right is None:
                self.right = newNode
            else:
                self.right.insert(newNode.value)
        else:
            if self.left is None:
                self.left = newNode
            else:
                self.left.insert(newNode.value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif self.value < target:
            if not self.right:
                return False

            return self.right.contains(target)

        elif self.value > target:
            if not self.left:
                return False

            return self.left.contains(target)

        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    #pre-order traversal: (root, left, right)
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)
        
        while queue:
            current = queue.pop(0)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            print(current.value)

            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while stack:
            current = stack.pop()

            if current.left:
                stack.append(current.left)
            if current.right: 
                stack.append(current.right)
            
            print(current.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
