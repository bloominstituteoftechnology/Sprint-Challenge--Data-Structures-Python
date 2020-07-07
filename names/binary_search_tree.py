
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take current value of our node (self.value)
        # compare to the new value we want to insert
        # think of base case where we don't need to recurse (here it's if self.left is None / self.left = BSTNode(value) and the right side as well)
        if value < self.value:  # compare value being passed in to node value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # if self.left is already taken by a node
                # make that node call insert - recursion
                # repeat function insert in this case until we reach base case
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:  # base case
            return True
        # which direction are we moving?
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

        # if current self.value  == target
        # return True
        # compare target to current value
        # if current value < target
        # check left subtree (self.left.contains(target))
        # if you cannot go left, return False
    # if current value >= target
        # check if right subtree contains target
        # if you cannot go right, return False

    # Return the maximum value found in the tree

  