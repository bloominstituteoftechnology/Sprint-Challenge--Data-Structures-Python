class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

''' Insert given value into tree . If no Node , insert new node . If Node , implement recursion . '''

''' If tree contains value , return TRUE . Return False otherwise . '''

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

''' Implement recursion '''
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            if self.right is None:
                return False
            return self.right.contains(target)