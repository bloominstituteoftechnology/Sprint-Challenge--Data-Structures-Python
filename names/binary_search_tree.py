import random

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        loop = True
        while loop == True:
            #   print(f'value[0]:{value[0]}')
            #   print(f'current.value[0]:{current.value[0]}')
            if value[0] > current.value[0]:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = BinarySearchTree(value)
                    loop = False
            elif value[0] < current.value[0]:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = BinarySearchTree(value)
                    loop = False
            elif value[0] == current.value[0]:
                if value[2] != current.value[2]:
                    current.value[1] += 1
                loop = False

    def for_each(self, cb, node="initial"):
        if node == "initial":
            node = self
        if node == None:
            return
        cb(node.value)
        self.for_each(cb, node.left)
        self.for_each(cb, node.right)
