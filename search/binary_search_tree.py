class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    cb(self.value)
    if self.left != None:
      if self.left:
        self.left.depth_first_for_each(cb)
        print(self.value)
    if self.right != None:
      if self.right:
        self.right.depth_first_for_each(cb)
        print(self.value)

  
  def breadth_first_for_each(self, cb):
    queue = []
    root_node = self.get_max()
    queue.append(root_node)

    while len(queue) != 0:
      queue[0].append()
      cb(self.value)
      if self.left != None:
        queue.append(self.left)
      if self.right != None:
        queue.append(self.right)

    
    
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
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

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
