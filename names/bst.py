class BinarySearchTree:
    def __init__(self, value):
        self.value = value #value of current node
        self.left = None #left subtree
        self.right = None #right subtree

    # Insert the given value into the tree
    def insert(self, value):
        #current node has no value
        if not self.value:
            self.value = value
            return
        #value is less than current node and no left subtree exists
        #initiate a left subtree with value
        elif value < self.value and not self.left:
            self.left = BinarySearchTree(value)
        #value is less than current node and left subtree exists
        #run insert on the left subtree
        elif value < self.value and self.left:
            self.left.insert(value)
        #value is greater than current node and no right subtree exists
        #initiate a right subtree with value
        elif value > self.value and not self.right:
            self.right = BinarySearchTree(value)
        #value is greater than current node and right subtree exists
        #run insert on the right subtree
        elif value > self.value and self.right:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check if current node is the target value
        if target == self.value:
            return True
        #target is less than current node and left subtree exists
        elif target < self.value and self.left:
            return self.left.contains(target)
        #target is greater than current node and Rigth subtree exists
        elif target > self.value and self.right:
            return self.right.contains(target)
        #target value does not equal current node value and no subtree exists
        else:
            return False