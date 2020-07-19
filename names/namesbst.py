class BSTNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, name):
        # I like to start with the easier inequality
        if name < self.name:
            # I prefer to start the loop with an assumed positive
            if self.left:
                # If there is a node on the left, we call this same insert function
                self.left.insert(name)
            
            else:
                # if there isn't, we add a node
                self.left = BSTNode(name)

        # Now we work on more than equal to
        else:
            if self.right:
                # Again, if there is already a node, call this same function
                self.right.insert(name)
            
            else:
                # Otherwise add a node
                self.right = BSTNode(name)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # First we check the node's value
        if self.name == target:
            return True
        
        # is target smaller?
        elif target < self.name:
            # is there a left node?
            if self.left:
                # if so, we call and return contains on it
                return self.left.contains(target)
                
            # if there isn't a left node
            else:
                return False
        
        # is it greater
        else:
            # is there a right node
            if self.right:
                # if so we call and return contains on it
                return self.right.contains(target)
                
            # if there isn't a right node
            else:
                return False