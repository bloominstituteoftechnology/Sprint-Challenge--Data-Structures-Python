class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        '''Inserts the given value into the tree'''
        newNode = BSTNode(value)
        if self.value <= newNode.value:
            if self.right is None:
                self.right = newNode
            else:
                self.right.insert(newNode.value)
        else:
            if self.left is None:
                self.left = newNode
            else:
                self.left.insert(newNode.value)
    def contains(self, target):
        '''
        Returns True if the tree contains the value\n
        False if it does not
        '''
        if self.value == target:
            return True
        elif self.value < target:
            if not self.right:
                return False
            return self.right.contains(target)
        elif self.value > target:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            return False


        