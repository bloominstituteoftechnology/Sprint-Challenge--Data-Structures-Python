
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # CASE 1: If value is less than self.value (left)
        if value < self.value:
            # If there is no left child, create node with the value there
            if self.left is None:
                self.left = BSTNode(value)
            # Else
            else:
                # Recursion: Repeat the process on the left subtree by calling insert again
                self.left.insert(value)

        # CASE 2: If value is greater than or equal than self.value (right)
        if value >= self.value:
            # if there is no right child, insert value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: Otherwise
        else:
            if self.right is None:
                return False
            else: 
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # No need to check left subtree
        # Will need to iterate through
        if self.right is not None:
            # if greater node exists, repeat
            return self.right.get_max()
        if self.right is None:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # if node exists to left
        if self.left is not None:
            self.left.for_each(fn)
        # if node exists to right
        if self.right is not None:
            self.right.for_each(fn)
