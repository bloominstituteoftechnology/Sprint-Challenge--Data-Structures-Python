"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # check if the value is less than the current node's value
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child
            # we can park the new node here
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check to see if the head is the equal to the target
        if self.value == target:
            return True

        else:
            # we want to compare the value to current node's value
            # if it is less than that node - than traverse through the left side
            if target < self.value:
                if self.left:
                    return self.left.contains(target)

            # it is is greater travere through the right side
            if target > self.value:
                if self.right:
                    return self.right.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # the max value is always going to be the right-most tree node
        if not self.right:
            return self.value
        return self.right.get_max()

        # Call the function `fn` on the value of each node

    def for_each(self, fn):
        #  call fn on self.value
        fn(self.value)
        # # check if self has a left child
        if self.left:
            #     # call `for_each` on the left child, passing in the fn
            self.left.for_each(fn)
        # # check if self has a right child
        if self.right:
            #     # call `for_each` on the right child, passing in the fn
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal


# testing for contains

# WORKING!!
# print(bst.contains(6))
# print(bst.contains(32))


# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# # bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
