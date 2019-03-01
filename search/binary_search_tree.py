class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # get a ref to the left and right nodes
        left = self.left
        right = self.right
        # return whatever cb is with the value
        cb(self.value)

        # if left node exists then recurs until it no longer does
        if left is not None:
            left.depth_first_for_each(cb)
        # if right node exists then recurs until it no longer does
        if right is not None:
            right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        left = self.left
        right = self.right
        cb(self.value)

        if left is not None:
            cb(left.value)
        if right is not None:
            cb(right.value)

        if left and left.left is not None:
            left.left.breadth_first_for_each(cb)
        if left and left.right is not None:
            left.right.breadth_first_for_each(cb)
        if right and right.right is not None:
            right.right.breadth_first_for_each(cb)
        if right and right.left is not None:
            right.left.breadth_first_for_each(cb)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
