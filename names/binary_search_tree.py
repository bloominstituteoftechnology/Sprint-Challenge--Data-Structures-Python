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

    def insert(self, value):
        #To-dos
        #check if empty
        #if empty put node here/at root  
        #else
          #if left doesn't exist
                #create left
            #else
                #leftnode.insert value
            #if right doesn't exist
                #create right
            #else
                #rightnode.insert value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else: #value is greater than or equal to
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #To-dos:
        #check tree for value at the root
        # if root node doesn't have the value, return false and move on
        # check branch on the right
        # if value is in a node on the right return true and break
        #else return false and go check the left node
        #if value is in a node on the left branch then return true and break
        if target == self.value:
            return True
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if target < self.value:
                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False



    # Return the maximum value found in the tree
    # in-class version of get_max using while loop
    def get_max(self):
        #To-dos
        #check if there is a right node -- if there is, get right
        # otherwise, get left 
        while self.right is not None:
            self = self.right
        
        return self.value

    # alternative method to do the get_max
    # def get_max(self):
    #     if self.right:
    #         return self.right.get_max()
    #     else:
    #         return self.value



    # Call the function `fn` on the value of each self
    def for_each(self, fn):
        #To-dos:
        #set the value of fn
        #if there is a left node, call the fn of each self on the left
        #otherwise do this on the right
       fn(self.value)
       
       if self.left:
           self.left.for_each(fn)

       if self.right:
           self.right.for_each(fn)




    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #To-dos:
        #check if node is empty
        #if not empty check right -- if not empty check right and left until you reach the final children
        #then recurse back to check the left
        if self.left is not None:
            self.left.in_order_print(self.left)
        
        print(node.value)

        if self.right is not None:
            self.right.in_order_print(self.right)
        



    # Print the value of every self, starting with the given self,
    # in an iterative breadth first traversal
    def bft_print(self, node):
    #To-dos
    # make a queue
    # add the root/starting node to queue, mark it as explored
    # as long as the queue is not empty node = head of queue
    # print
    # dequeue from the front of the queue, this is our current node
    # enqueue the kids of the current node into the queue
    # pop node off the queue

            
        queue = []
        # print(node)
        queue.append(node)

        while(len(queue) > 0):
            node = queue.pop(0)
            # print(queue[0].value)
            # print(len(queue))
            print(node.value)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        
           

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
    #To-dos:
    # make a stack -- push the head node on the stack
    # loop and and check if the stack is empty -- as long as the stack is not empty...
    ## pop off the stack -- this is the current_node
    ## put the kids of the current node the stack
    ## (check that they are not None -- then put them on the stack)
        stack = []
        stack.append(node)
        while len(stack) != 0:
            node = stack.pop()
            print(node.value)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

    

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# t = BSTNode(1) #or what your tree class is named
# t.insert(8)
# t.insert(5)
# t.insert(7)
# t.insert(6)
# t.insert(3)
# t.insert(4)
# t.insert(2)
# t.bft_print(t)