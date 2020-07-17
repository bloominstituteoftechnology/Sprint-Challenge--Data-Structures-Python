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
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    #Insert value into tree
    def insert(self, value):
        if value < self.value:
            #If no left child, insert value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        
    
    def containsDups(self, target):
        if target == self.value:
            return True
        if target >= self.value:
            if self.right == None:
                return False
            else:
                return self.right.containsDups(target)
        else:
            if self.left == None:
                return False
            else:
                return self.left.containsDups(target)

BST = BSTNode("names")


for name_1 in names_1:
    BST.insert(name_1)
    
for name_2 in names_2:
    if BST.containsDups(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


##original runtime = 6.6036 seconds
#New 0.136
# Runtime is O(n log n)
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
