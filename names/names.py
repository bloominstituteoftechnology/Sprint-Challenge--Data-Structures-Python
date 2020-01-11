import time

# using Binary Search Tree data strcuture to hold names names
# only insert & contains are needed
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if new value is less than current node
        if value < self.value:
            # there is NO self.left value
            if not self.left:
                # set NEW left child as as new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)    
        # the new value is greater than the current node
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)    


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True
        # target is smaller, go left
        sub_tree_contains = False
        if target < self.value:
            if not self.left:
                return False
            else:
                #return self.left.contains(target)
                sub_tree_contains = self.left.contains(target)        
        # target is larger, go right
        else: 
            if not self.right:
                return False
            else:
                sub_tree_contains = self.right.contains(target)    
        # must return something
        return sub_tree_contains



start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Double for loops cause a nasty complexity of O(n^2),  run takes about 6 secs 
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
