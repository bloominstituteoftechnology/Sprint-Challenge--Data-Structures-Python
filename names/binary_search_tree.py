
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        while node:
            
            if value[1] < node.value[1]:
                if node.left:
                    node = node.left
                else:
                    node.left = BinarySearchTree(value)
                    return

            elif value[1] >= node.value[1]:
                if node.right:
                    node = node.right
                else:
                    node.right = BinarySearchTree(value)
                    return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        node = self
        while node is not None:

            if target[0] == node.value[0]:
                
                return True 
            elif target[1] >= node.value[1]:
                
                if node.right:
                    node = node.right 
                else:        
                    return False 
            elif target[1] < node.value[1]:
                
                if node.left:
                    node = node.left
                else:
                    return False

        return False