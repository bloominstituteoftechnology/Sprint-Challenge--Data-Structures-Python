import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates= []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        #find value
        if self.value == value:
            duplicates.append(value)
            return
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else: 
                self.left = BSTNode(value)
                
 
        else:
            if self.right is not None:
                self.right.insert(value)
            else: 
                self.right = BSTNode(value)

tree = BSTNode(names_1[0])
for name_1 in names_1[1:]:
    tree.insert(name_1)
    
for name_2 in names_2:
    tree.insert(name_2)


                    
            

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
