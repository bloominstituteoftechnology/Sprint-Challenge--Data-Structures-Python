import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
​
    # Insert the given value into the tree
    def insert(self, value):
        # check if the incoming value is less than the current node's value 
        if value < self.value:
            # we know we need to go left 
            # how do we know when we need to recurse again, 
            # or when to stop? 
            if not self.left:
                # we can park our value here 
                self.left = BSTNode(value)
            else:
                # we can't park here 
                # keep searching 
                self.left.insert(value)
        else:
            # we know we need to go right 
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
​
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # 
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)
​
    # Return the maximum value found in the tree
    def get_max(self):
        # we'll keep going right until there are no more nodes on the right side 
        if not self.right:
            return self.value
        # otherwise, keep going right 
        return self.right.get_max()
​
    def iterative_get_max(self):
        current_max = self.value 
​
        current = self
        # traverse our structure
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            # update our current_max variable if we see a larger value 
            current = current.right
​
        return current_max
​
    # Call the function `fn` on the value of each node
    # Do we expect a return from the for_each function? No 
    def for_each(self, fn):
        # call the fn on the value at this node 
        fn(self.value)
​
        # pass this function to the left child 
        if self.left:
            self.left.for_each(fn)
        # pass this function to the right child 
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
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

node = BSTNode('')

for name in names_1:
    node.insert(name)
    
for name in names_2:
    if node.contains(name)
    duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
