class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.max = 0

    def insert(self, value):
        
        leaf = BinarySearchTree(value)
        if value < self.value:
            if self.left:
                leaf = self.left.insert(value)
            else:
                self.left = leaf

        # dupe needs reassignment, interesting to consider context for reassignment of same vals
        elif value >= self.value:
            if self.right:
                leaf = self.right.insert(value)
                self.max = value

            else:
                self.right = leaf
                self.max = value
        return leaf
        
    def contains(self, target):
    
        if target == self.value:
            return True

        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        
    def get_max(self):
        
        self.max = self.value if self.value > self.max else self.max
        return self.max

    def for_each(self, cb):

        if self.left is not None:
            self.left.for_each(cb)

        if self.right is not None:
            self.right.for_each(cb)

        cb(self.value)
        
    def in_order_print(self, node):
        
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)       




# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# assert bst.contains(4),True

# bst.in_order_print(bst)

# print('\n\n\n')

# bst.bft_print(bst)

# print('\n\n\n')

# bst.dft_print(bst)

# print('\n\n\n')

# bst.post_order_dft(bst)

# print('\n\n\n')

# bst.pre_order_dft(bst)