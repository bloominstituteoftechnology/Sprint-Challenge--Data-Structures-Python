from queue import Queue
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
        if self.value == None:
            self.value = BSTNode(value)
        # if value is less than current, move left
        elif value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # if value is more than or equal to current, move right
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the target entered is the the root, return True
        if target == self.value:
            return True
        # save the target to be updated in a loop
        curr_value = target
        # keep track of current iteration of nodes
        current_node = self
        while current_node != None:
            # if its the current number, return True
            if current_node.value == curr_value:
                return True
            # if its less than, move left
            elif curr_value < current_node.value:
                current_node = current_node.left
            # if its equal to or greater than, move right
            elif curr_value >= current_node.value:
                current_node = current_node.right
            # if its None, return False
            else:
                return False
        
    # Return the maximum value found in the tree
    def get_max(self):
        # if root is the only node, return value
        if self.right == None:
            return self.value
        
        # hold value
        max_value = self.value
        current_node = self
        # loop as long as theres a node to the right
        while current_node != None:
            max_value = current_node.value
            current_node = current_node.right
                       
        # return max_value
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # 1. Base case - no more nodes in our subtree
        # 2. Recursive case
        fn(self.value)

        if self.left is not None: # if self.left
            self.left.for_each(fn)
        if self.right is not None: # if self.right
            self.right.for_each(fn)

    # STRETCH
    def delete(self, value):
        # search like in contains()
        curr_node = self
        # if node at bottom level

            # update parent left/right

        # if node has only 1 child

            # parent.left/right = curr_node.left/right
        
        # if node has two children

            # 'greater'(right?) child needs to become new parent
            
        
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # if curr node is null; pass
        if self.value is None:
            pass

        # check left. if there is something left, go recurse
        if self.left is not None:
            self.left.in_order_print()
        # after moving as far left as possible, we print curr node value
        print(self.value)

        # check right. if there is something right, recurse
        if self.right is not None:
            self.right.in_order_print()

        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = Queue()
        q.enqueue(self)

        while q.__len__() != 0:
            current = q.dequeue()
            print(current.value)
            if current.left is not None:
                q.enqueue(current.left)
                
            if current.right is not None:
                q.enqueue(current.right)
                

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        queue = []
        current = None

        if not self.value:
            pass

        queue.append(self)

        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)

        print(queue.pop(0).value)

        current = queue[0]

        while current != None:
            
            if current.right:
                queue.insert(1, current.right)
            if current.left:
                queue.insert(1, current.left)
            
            if len(queue) > 0:
                print(queue.pop(0).value)

                if len(queue) > 0:
                    current = queue[0]
                else:
                    current = None