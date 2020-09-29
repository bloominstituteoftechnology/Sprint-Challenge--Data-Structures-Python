class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)



            # pass
        # look at root, if root is taget return true
        # if target == self.value:
        #     return True
        # # if value is less than node
        # elif target < self.value:
        #     # go left
        #     if self.left != None:
        #         # return if found
        #         return self.left.contains(target)
        # # if value is greater or equal to node
        # elif target >= self.value:
        #     # go right
        #     if self.right != None:
        #         # return if found
        #         return self.right.contains(target)
        # # else return false
        # else:
        #     return False