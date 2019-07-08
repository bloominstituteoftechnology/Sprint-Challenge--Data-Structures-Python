import time

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value >= self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)
    elif value < self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
        

  def contains(self, target):
    if target == self.value:
      return True

    if target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    if target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False



  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n") # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n") # List containing 10000 names
f.close()

duplicates = []
tree = BinarySearchTree(names_1[0])
for name in names_1:
    tree.insert(name)
for name in names_2:
    if tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Starting runtime was at about 6.6 seconds
# New runtime at about 0.16 seconds