class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

    # insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                # if node does not exist, insert new node
                self.left = BinarySearchTree(value)
            else:
                # if node exists, recurse
                self.left.insert(value)
        else:
            # value is >= node
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # recursive solution
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            if self.right is None:
                return False
            return self.right.contains(target)