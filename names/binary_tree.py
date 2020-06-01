class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        node = self
        while node.value != target:
            if node.value < target:
                node = node.right
            else:
                node = node.left
            if node is None:
                return False
        return True           