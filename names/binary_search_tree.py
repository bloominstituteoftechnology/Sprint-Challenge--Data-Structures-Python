''' things to remember. if you want to:
delete - you must traverse
on delete - smallest child becomes the parent
>= flows right '''


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    ''' on insert, it adds the input value to the BST
        it follows the rules of the order of elements
        in order to find your insertion spot, you need to traverse'''

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    ''' 'contains' will search the BST for the input value
        a boolean will be returned to confirm the value exists or not
        Traverse the tree by starting at the root
        On finding the first instance of the value - stop (return true)
        if the search reaches a node that doesn't have children - then the value is not found (reutrn false)'''

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:

            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)

    ''' 'get max' will return max value in the BST
         search moves right until it can go no further'''

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    ''' 'for each' traverses every node in the tree
         executes the passed-in callback func on each node '''

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        cb(self.value)

        if self.right != None:
            self.right.for_each(cb)

        if self.left != None:
            self.left.for_each(cb)
