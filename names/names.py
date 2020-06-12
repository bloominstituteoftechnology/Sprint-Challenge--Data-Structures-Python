class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = TreeNode(value)
    else:
      if self.left:
        self.left.insert(value)
      else:
        self.left = TreeNode(value)

  def contains(self, target):
    current_node = self
    while current_node.value != target:
      if current_node.value > target:
        if current_node.left:
          current_node = current_node.left
        else:
          return False
      else:
        if current_node.right:
          current_node = current_node.right
        else:
          return False
    return True

#---------------------------------------------------------------

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n") 
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
names_tree = TreeNode(names_1[0])
for name in names_1[1:]:
	names_tree.insert(name)

for name in names_2:
    if names_tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time = time.time()

file = open('names_1.txt', 'r')
names_1 = file.read().split("\n") 
file.close()

file = open('names_2.txt', 'r')
names_2 = file.read().split("\n") 
file.close()

dupes = []
names_set = set(names_1) #reArranes iterables in order, an some how increases speed by 1.0322

for name in names_2:
    if name in names_set:
        dupes.append(name)

end_time = time.time()
print (f"{len(dupes)} duplicates:\n\n{', '.join(dupes)}\n\n")
print (f"fastest runtime: {end_time - start_time} seconds")