import time

# use binary search tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check whether new nodes value is less than current nodes value
        if value < self.value: 
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        # check weather new nodes value is greater or equal to current node
        elif value >= self.value:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)

   # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left else False
        else:
            return self.right.contains(target) if self.right else False 
    
    # Return the maximum value found in the tree
    def get_max(self):
        # The largest value will always be on the right of the current node
        #  if we can go right lets find the largest number by calling get_max on the right subtree
        #  of we cannot go right retrun the current value
        if self.right is None:
            return self.value
        max_val = self.right.get_max()
        return max_val
    
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call function on the current value fn(self.value)
        fn(self.value)
        # if you can go left, call for_each on the left tree 
        if self.left:
            self.left.for_each(fn)
        #  if you can go right call for_each on the right tree
        if self.right:
            self.right.for_each(fn)

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

# n = BST(names_1[0])
# for i in range(1, len(names_1)):
#     n.insert(names_1[i])

# for i in names_2:
#     if n.contains(i):
#         duplicates.append(i)

duplicates = set.intersection(set(names_1),set(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
