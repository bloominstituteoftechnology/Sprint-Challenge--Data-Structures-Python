class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb, stack=[], visited=[]):
    #Preorder (Root, Left, Right)
    # stack = []
    # visited = []

    if len(stack) == 0:
      if self not in visited:
        stack.append(self)

    if len(stack) > 0:
      #pop last item from stack
      node = stack.pop()
    
      #add to visited
      visited.append(node.value)
      
      cb(node.value)

      #add its children to the stack, check if left child has value
      # if it does, do recursive call on its left value
      if self.left:
        stack.append(self.left)
        self.left.depth_first_for_each(cb, stack, visited)
      # if it does not, do recursive call on its right child
      if self.right:
        stack.append(self.right)
        self.right.depth_first_for_each(cb, stack,visited)
    # print(stack)
    return visited

 
  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        print(f'{value} is less than {self.value}. inserting in left side of {self.value}')
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        print(f'{value} is greater than {self.value}. inserting in right side of {self.value}')
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    current_val = self.value
    print(self.value, target)
    if current_val == target:
      return True
    if self.left is None and self.right is None and current_val is not target:
      return False
    if self.right is not None and target > current_val:
      return self.right.contains(target)
    if self.left is not None and target < current_val:
      return self.left.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value



import time
start_time = time.time()

# names_1 = BinarySearchTree('M')
# names_2 = BinarySearchTree('M')


names_dict = {}

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # O(n) operation to store names in dictionary ,  List containing 10000 names
for name in names_1:
    names_dict[name] = name
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # O(n) operation to store names in list List containing 10000 names
f.close()

duplicates = []
for name in names_2:       #O(n) operation to loop through all names in list
    if name in names_dict:   #O(1) operation to check if exists in dict
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

