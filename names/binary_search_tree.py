import sys
# sys.path.append('../GitHub/Data-Structures/queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
            # return self.value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self.value is None:
        #     return False
        # if self.value == target:
        #     return True
        # else:
        #     if target < self.value:
        #         return self.left.contains(target)
        #     else:
        #         return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True
    # Return the maximum value found in the tree
    def get_max(self):
        if self.value == None:
            return None
        # maxvalue = self.value
        if self.right == None:
            if self.left != None:
                return self.left.get_max()
        if self.right != None:
            return self.right.get_max()
        return self.value
        
        # else:
        #     self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)