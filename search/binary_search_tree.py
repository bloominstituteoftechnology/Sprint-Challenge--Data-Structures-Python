class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    cb(self.value)
    if self.left != None:
      self.left.depth_first_for_each(cb)
    if self.right != None:
      self.right.depth_first_for_each(cb)
    return


  def breadth_first_for_each(self, cb):
    nodes = [self]
    #while loop going through every node
    while len(nodes) > 0:
      current = nodes.pop(0)
      cb(current.value)
      if current.left != None:
        nodes.append(current.left)
      if current.right != None:
        nodes.append(current.right)


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
