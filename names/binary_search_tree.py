class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if self.value == value:
            return True
        if value < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(value)                                            
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(value)    