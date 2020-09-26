class BinarySearchTree:
    def __init__(self, value):
        self.value = value #value of current node
        self.left = None #left side
        self.right = None #right side

    #insert value
    def insert(self, value):
        #no value
        if not self.value:
            self.value = value
            return
        #value is < current and no left side
        #start left side
        elif value < self.value and not self.left:
            self.left = BinarySearchTree(value)
        #value is less and left exists
        elif value < self.value and self.left:
            self.left.insert(value)
        #value is > current and no right
        #start right
        elif value > self.value and not self.right:
            self.right = BinarySearchTree(value)
        #value > and right exists
        elif value > self.value and self.right:
            self.right.insert(value)

    #return true if contains value
    #false if not
    def contains(self, target):
        #check if current node is target
        if target == self.value:
            return True
        #target < current and left exists
        elif target < self.value and self.left:
            return self.left.contains(target)
        #target > current and right exist
        elif target > self.value and self.right:
            return self.right.contains(target)
        #target value does not equal current and no trees
        else:
            return False