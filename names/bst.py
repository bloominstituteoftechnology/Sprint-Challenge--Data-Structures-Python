
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                new_node = BSTNode(value)
                self.right = new_node
        else:
            if self.left:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node

    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return self.left.contains(target) if self.left else False

    def get_max(self):
        max = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max

    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
