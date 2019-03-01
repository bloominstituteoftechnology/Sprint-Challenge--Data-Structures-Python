class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    # a container to keep track of insertion order
    # start with first value inserted during creation
    self.order = [value]

  def depth_first_for_each(self, cb):
    # if order container is not empty
    if self.order:
      # apply cb to all nodes
      [cb(n) for n in self.order]


  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
        # store value after after setting left node
        self.order.append(value)
      else:
        self.left.insert(value)
        # store value after sending value off to left subtree
        self.order.append(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
        # store value after setting right node
        self.order.append(value)
      else:
        self.right.insert(value)
        # store value after sending value off to right subtree
        self.order.append(value)

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

