class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # recurse to the left
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                # recurse to the right

            else:
                self.right.insert(value)

 
    def contains(self, target):

        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                # recurse
                self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)


    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)
