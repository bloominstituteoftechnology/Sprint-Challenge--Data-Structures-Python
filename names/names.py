#(This implementation runs at O(n^2) due to the nested for loops. The complexity is directly
# proportional to the square of the input size. In this case, we iterate through name_1's 10,000
# elements, comparing them to name_2's 10,000 elements, giving us 10,000^2 operations. 

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# My Implementation using a Binary Search Tree
# This implementation will give us O(log n) complexity due to its improved search ability.
# I also insert directly into the tree as opposed to creating a seperate variable and inserting
# from there. This saves .01 seconds. Woohoo!

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Left side
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        # Right side
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check root
        if target == self.value:
            return True
        #check subleft nodes:
        elif target < self.value and self.left:
                return self.left.contains(target) 
        #check subright nodes:
        elif target > self.value and self.right:
                return self.right.contains(target)

start_time = time.time()

# instantiate tree
tree = BSTNode("")

f = open('names_1.txt', 'r')
# add values to tree
for name in f.read().split("\n"):
    tree.insert(name)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

my_duplicates = []  # Return the list of duplicates in this data structure

#check for duplicates from second list
for name in names_2:
    if tree.contains(name):
        my_duplicates.append(name)

end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")

# elements would not appear in same order, so sorting required to assert equality
assert my_duplicates.sort() == duplicates.sort()


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
