
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # insert
        # left case
        # check if our value is less than root value
        if value < self.value:
            # move to the left and check if it is None
            if not self.left:
                # insert node here set the self.left to the new node
               self.left = BSTNode(value)
            # otherwise
            else:
                # do an insert on the root's left node recursive call to the left node using self.left
                return self.left.insert(value)
        # right case
        # otherwise
        else:
            # move to the right and check if it is None
            if self.right is None:
                # insert node here set the self.right to the new node
               self.right = BSTNode(value)
            # otherwise
            else:
                # do an insert on the root's right node recursive call to insert using self.right
                return self.right.insert(value)
      

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
         # contains
        # check the value root node (self.value) against the target
        # if the root node value and target are the same
        if self.value == target:
            # return True
            return True
        
        # left case
        # check if our target is less than the root val (self.value)
        elif target < self.value:
            # check if there is no child to the left (self.left) is None
            if not self.left :
                # return False
                return False
            # otherwise
            else:
                # call contains on the left child (self.left)
                return self.left.contains(target)
        
        # right case
        # otherwise
        else:
            # check if there is no child to the right (self.right) is None
            if not self.right:
                # return False
                return False
            # otherwise
            else:
                # call contains on the right child (self.right)
                return self.right.contains(target)

