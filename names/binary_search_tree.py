# Utilize the BST from the hw assignment
# Only need contains and insert methods

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # Compare the input value against the node's value
    # Check if the direction we need to go in has a node
        #  If not, wrap the value in a node and park it
        #  Otherwise, go back to step 1, but with the node in that spot

    # This doesn't work if there is no root

    def insert(self, value):
        # Compare the input value with the value of the Node
        if value < self.value:
            # We need to go left
            # If there is no child node to the left
            if self.left is None:
                # Create and park the new node
                self.left = BSTNode(value)

            # Otherwise there is already a child
            else:
                # Call the insert method to do this loop again, until we reach no child node
                self.left.insert(value)
        
        # If the input value is greater than or equal to we move to the right
        else:
            # See if there is no right child
            if self.right is None:
                # Wrap the value in BSTNode and park it
                self.right = BSTNode(value)

            # Otherwise there is a child node
            else:
                # Call the insert method to continue the loop until we find a node without a child
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If the input value is equal to the node value, return true
        # Base Case
        if self.value == target:
            return True

    # Recursive cases: How do we move closer to the base case
        
        # If the input value is greater than the node value, move to the right -> re-run method on right child node
        elif self.value < target:
            # Check if there is a next node to move to to continue the comparison
            # If there is not then it is the end of the tree and there is no match, return False
            if self.right is None:
                return False
            else:
                # Call contains method on right child
                # Eventually we will need to return a value
                return self.right.contains(target)

        # If the input value is less than the node value, move to the left -> re-run method on left child node
        else:
            # Check to see if there is a node to the left to move to
            # If not then it is the end of the tree, return False
            if self.left is None:
                return False
            else: 
                # Call contains method on left child
                # Eventually we will need to return a value  
                return self.left.contains(target)
