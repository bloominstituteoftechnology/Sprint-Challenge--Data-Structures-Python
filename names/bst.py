class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def in_order_print(self, node=None):
        if self is None:
            return

        # check if we can move left
        if self.left is not None:
            self.left.in_order_print()

        # print node value
        print(self.value)

        # check if we can move right
        if self.right is not None:
            self.right.in_order_print()

        print(self.value)
