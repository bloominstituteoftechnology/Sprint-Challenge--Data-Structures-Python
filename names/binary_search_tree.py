class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        # 1. is the new node's value is less than the current value? Go left
        # a. Is there a child? If not, insert value
        # b. if there is a child, repeat process
        # 2. if the new node's value is greater than the current value? Go right
        # a. is there a child? If not, insert value
        # b. if there is a child Repeat the process

    def insert(self, value):
        if value < self.value:  # Check if the new nodes value is less than the current value
            if not self.left:  # go left
                self.left = BinarySearchTree(value)  # repeat search
            else:
                self.left.insert(value)  # insert the value
        else:
            if not self.right:  # go right
                self.right = BinarySearchTree(value)  # repeat search
            else:
                self.right.insert(value)  # insert the value

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:

            if not self.left:  # look left
                return False
            return self.left.contains(target)
        else:

            if not self.right:  # look right
                return False
            return self.right.contains(target)

    def get_max(self):
        while self.right is not None:
            max = self.value
            self = self.right
        max = self.value
        return max

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
            cb(self.value)
        if self.right:
            self.right.for_each(cb)
