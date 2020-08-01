import time


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check whether new node's value is less than current node's value
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # check whether new node's value is greater than or equal to curr node's val
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check whether curr node matches target
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # U: traverse BST to find global max
        # 1. check your input --> is there a node here?
        # 2. declare max variable == self.value
        # 3. iterate through tree until we hit Null
        # 4, update max value
        # 5. move to the right

        # if not self:
        #     return None
        # max_value = self.value
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value

        # recursive solution................................
        # base case: no right node available
        # recursive step: move to the right to get_max

        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if not self:
            return
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        if not self:
            return
        # left -> root -> right
        if self.left:
            self.left.in_order_print()
        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # 1. define deque
        # 2. add self to deque
        # 3. iterate: while there are items in the deque
        # 4. dequeue/pop from deque, point to result, and print
        # 5. add left and right children to deque
        qq = deque()
        qq.append(self)
        while len(qq) > 0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = []
        s.append(self)
        while len(s) > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # 0. check input
        # ROOT -> LEFT -> RIGHT
        # 1. recurse to the left
        # 2.  recures to the right
        # 3. print self
        if not self:
            return
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
            # print(self.left.value)
        if self.right:
            self.right.pre_order_dft()
            # print(self.right.value)

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # 0. check self
        # left -> right -> root
        # 1. recurse to the left
        # 2. recurse to the right
        # 3. print self
        if not self:
            return
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
name1_bst = BSTNode("Names One Tree")
for name1 in names_1:
    name1_bst.insert(name1)
for name2 in names_2:
    if name1_bst.contains(name2):
        duplicates.append(name2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
