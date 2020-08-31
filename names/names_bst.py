class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_value = BinarySearchTree(value)
        if not self.value:
            return new_value
        if value < self.value:
            if not self.left:
                self.left = new_value
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_value
            else:
                self.right.insert(value)

    def contains(self, target):
        if not self.value:
            return False
        if target == self.value:
            return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    def get_max(self):
        if not self.value:
            return None
        if self.right:
            return self.right.get_max()
        else:
            return self.value
    
    def for_each(self, cb):
        if not self.value:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
                