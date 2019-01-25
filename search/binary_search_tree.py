class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        if self.value is not None:
            # Running function on initial value
            cb(self.value)
            if self.left is not None:
                self.left.depth_first_for_each(cb)
            if self.right is not None:
                self.right.depth_first_for_each(cb)
        else:
            pass

    def breadth_first_for_each(self, cb):
        pass
        # start from the bottom of the tree
            #How do we start from the bottom of the tree?
        # traverse our way upward calling cb on each node
        # return that array'
        # c = BinarySearchTree.copy_tree(self)
        # for item in c:
        #     cb(item)
        # return c

    def copy_tree(self, copied=[]):
        if self.value is not None:
            copied.append(self.value)
            if self.left is not None:
                self.left.copy_tree(copied)
            if self.right is not None:
                self.right.copy_tree(copied)
        return copied

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if value < self.value:
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
