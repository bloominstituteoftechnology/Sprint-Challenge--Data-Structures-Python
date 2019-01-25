import time
import sys
sys.path.append('../search')
#from binary_search_tree import BinarySearchTree

start_time = time.time()

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    direction = "right" if value > self.value else 'left' 
    if getattr(self, direction) is None:
      setattr(self, direction, BinarySearchTree(value))
      return
    else:
      self = getattr(self,direction)
    
    self.insert(value)
    pass
    
    
  def contains(self, target):
    if target == self.value:
      return True

    if target < self.value:
      if self.left is None:
        return False
      else:
        self = self.left
    elif target > self.value:
      if self.right is None:
        return False
      else:
        self = self.right
    
    return self.contains(target)
    

  def get_max(self):
    while self.right is not None:
      self = self.right
    return self.value
    pass


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
bst_1 = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    bst_1.insert(name)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name in names_2:
    if bst_1.contains(name):        
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

