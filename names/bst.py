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

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is not None:
            if value < self.value:
                if self.left is not None:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            elif value > self.value:
                if self.right is not None:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)
            elif value == self.value:
                new_node = BSTNode(value)
                new_node.right = self.right
                self.right = new_node
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target): # recursive depth-first search
        if self.value == target:
            return True
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        else: # leaf with no children but not the target value
            return False

    # Return the maximum value found in the tree
    def get_max(self): # go all the way right
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    def get_min(self):
        if self.left is not None:
            return self.left.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn): # recursive preorder depth-first action
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    def in_order_dft(self):
        if self.left is not None:
            self.left.in_order_dft()
        print(self.value)
        if self.right is not None:
            self.right.in_order_dft()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        bft_set = self.bf_traverse(0)
        for level in bft_set:
            for value in bft_set[level]:
                print(value)

    def bf_traverse(self, level=0):
        bft_set = {}
        bft_set[level] = [self.value]
        if self.left is not None:
            left_set = self.left.bf_traverse(level+1)
            for left_level in left_set:
                # if bft_set[left_level] is not None:
                if left_level in bft_set:
                    bft_set[left_level].extend(left_set[left_level])
                else:
                    bft_set[left_level] = left_set[left_level]
        if self.right is not None:
            right_set = self.right.bf_traverse(level+1)
            for right_level in right_set:
                # if bft_set[right_level] is not None:
                if right_level in bft_set:
                    bft_set[right_level].extend(right_set[right_level])
                else:
                    bft_set[right_level] = right_set[right_level]
        # print(f"Level: {level}, set: {bft_set}")
        return bft_set

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        print(self.value)
        if self.left is not None:
            self.left.dft_print()
        if self.right is not None:
            self.right.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft()
        if self.right is not None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left is not None:
            self.left.post_order_dft()
        if self.right is not None:
            self.right.post_order_dft()
        print(self.value)
