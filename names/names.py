import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        while True:
            if value >= node.value:
                if(node.right != None):
                    node = node.right
                else:
                    #needs to be inserted to the right
                    node.right = BinarySearchTree(value)
                    break
            else:
                if(node.left != None):
                    node = node.left
                else:
                    node.left = BinarySearchTree(value)
                    break
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        while node != None:
            if target == node.value:
                return True
            else:
                if target > node.value:
                    node = node.right
                else:
                    node = node.left
        return False

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
b = BinarySearchTree(names_1[0])

for i in range(1, len(names_1)):
    b.insert(names_1[i])

for j in names_2:
    if b.contains(j):
        duplicates.append(j)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# A set would be a good tool to use as it's lookup time is O(1), so add first list to the set - O(n)
# go through second array checking if elements exist in the set, would be O(m). so O(m + n) 