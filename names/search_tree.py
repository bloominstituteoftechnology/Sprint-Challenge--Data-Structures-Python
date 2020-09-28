class BSTNode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self, value):
        if self.value is None:

            self.value = value
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if self.value == target:
            print(f"Made it with {target}")
            return True
        elif target < self.value and self.left:

            return self.left.contains(target)
        elif target > self.value and self.right:

            return self.right.contains(target)

        return False
