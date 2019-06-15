import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = set(names_1) & set(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

### Stretch ###

start_time2 = time.time()

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value > self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif self.right is None and self.left is None:
      return False
    else:
      if self.left is not None:
        if self.left.contains(target):
          return True
      if self.right is not None:
        if self.right.contains(target):
          return True

namesOne = BinarySearchTree('Abi')

for i in names_1:
    namesOne.insert(i)

common = []

for i in names_2:
    if namesOne.contains(i):
        common.append(i)

end_time2 = time.time()

###Hahaha - works, but not at all efficient
print(common)
print (f"runtime: {end_time2 - start_time2} seconds")


