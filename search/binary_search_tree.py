class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  def breadth_first_for_each(self, cb):
    queue = [self]
    while queue: # O(n)
      vertex = queue.pop(0) 
      if vertex.value:
        cb(vertex.value)
        if vertex.right:
          if vertex.left:
            queue.append(vertex.left)
            queue.append(vertex.right)
          else:
            queue.append(vertex.right)
    return
    
  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

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


# bst = BinarySearchTree(5)
# bst.insert(3)
# bst.insert(4)
# bst.insert(10)
# bst.insert(9)
# bst.insert(11)

# print(bst.contains(5))
# print(bst.contains(3))
# print(bst.contains(4))

# arr = []
# cb = lambda x: arr.append(x)

# bst.breadth_first_for_each(cb)
# print(arr)


