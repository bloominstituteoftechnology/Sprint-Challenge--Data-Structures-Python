import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                new_node = BSTNode(value)
                self.right = new_node
        else:
            if self.left:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        
        else:
            return self.left.contains(target) if self.left else False

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
# names_1 = sorted(names_1)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
# names_2 = sorted(names_2) 
f.close()

# duplicates = sorted(names_1 + names_2, key=lambda x: x.split(" ")[-1])  # Return the list of duplicates in this data structure
duplicates = []


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

root_node = BSTNode(names_1[0])
for name in names_1:
    root_node.insert(name)
for name2 in names_2:
    if root_node.contains(name2):
        duplicates.append(name2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
