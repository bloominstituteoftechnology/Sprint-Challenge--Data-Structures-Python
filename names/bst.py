'''
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. '''

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare the current value of the node(self.value)
        if value < self.value:
            #insert the value in left
            if self.left is None:
                # insert node value if no node in the left side
                self.left = BSTNode(value)
            else:
                # repeat the  process for the next node
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right =BSTNode(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target ==self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        if target >=self.value:
            if self.right is None:
                return False
            else:
                 return self.right.contains(target)