class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = BSTNode(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = BSTNode(value)
                    break

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        while True:
            if target == current.value:
                return True
            if target < current.value:
                if current.left:
                    current = current.left
                else:
                    return False  
            else:
                if current.right:
                    current = current.right
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        max_value = self.value
        while True:
            if current.right:
                current = current.right
                max_value = current.value
            else:
                return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)