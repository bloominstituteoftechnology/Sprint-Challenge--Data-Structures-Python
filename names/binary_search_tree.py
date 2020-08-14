
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < Node's value
        if value < self.value:
            # we need to go left 
            # if we see that there is no left child, 
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the left child's `insert` method 
                self.left.insert(value)
        # otherwise, value >= Node's value 
        else:
            # we need to go right 
            # if we see there is no right child, 
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it 
                self.right = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the right child's `insert` method 
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # 1. base case 
        # if the value of this node matches the target, then we've found
        # what we're looking for 
        if self.value == target:
            return True
        # 2. "how do we move closer to the base case?"
        # compare the target against this node's value to determine which 
        # direction we need to go in 
        if target < self.value:
            # we need to go left 
            # what if there is no left child? 
            if not self.left:
                # then the value can't be in the tree 
                return False
            # what if there is? 
            else:
                # call `contains` on the left child 
                return self.left.contains(target)
        else:
            # we need to go right
            # what if there is no right child? 
            if not self.right:
                # then the value can't be in the tree 
                return False
            # what if there is? 
            else:
                # call `contains` on the right child 
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # the max value in the tree will always be the right-most value 
        # recursive 
        # we'll just keep going right until there is no right child node 
        # base case: there is no right child 
        # if not self.right:
        #     return self.value
        # # otherwise, call `get_max` on the right child 
        # return self.right.get_max()

        # iterative 

        # keep a `current` pointer to keep track of where we
        # are in the tree 
        current = self

        # iterate down the right child of the current node 
        while current.right is not None:
            # until we no longer have a right child to go to  
            current = current.right

        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the anonymous function on `self.value`
        fn(self.value)

        # if this node has a left child 
        if self.left:
            # pass the anonymous fn to it 
            self.left.for_each(fn)
        # if this node has a right child 
        if self.right:
            # pass the anonymous fn to it 
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO 
        # we'll use a stack 
        stack = []
        stack.append(self)

        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack 
            current = stack.pop()

            # add the current node's right child first 
            if current.right:
                stack.append(current.right)

            # add the current node's left child 
            if current.left:
                stack.append(current.left)

            # call the anonymous function 
            fn(current.value)

    def iterative_breadth_first_for_each(self, fn):
        from collections import deque

        # BFT: FIFO 
        # we'll use a queue to facilitate the ordering 
        queue = deque()
        queue.append(self)

        # continue to traverse so long as there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            fn(current.value)