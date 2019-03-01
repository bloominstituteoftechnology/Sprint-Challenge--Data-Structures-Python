class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    parent_node = self
    left_node = self.left
    right_node = self.right
    cb(parent_node.value)

    if left_node is not None:
      left_node.depth_first_for_each(cb)
    if right_node is not None:
      right_node.depth_first_for_each(cb)


  def breadth_first_for_each(self, cb):
    parent_node = self
    left_node = self.left
    right_node = self.left
    cb(parent_node.value)
    if left_node is not None:
      cb(left_node.value)
    if right_node is not None:
      cb(right_node.value)

    if hasattr(left_node, "left") and left_node.left is not None:
      left_node.left.breadth_first_for_each(cb)
    if hasattr(left_node, "right") and left_node.right is not None:
      left_node.right.breadth_first_for_each(cb)
    if hasattr(right_node, "left") and right_node.left is not None:
      right_node.left.breadth_first_for_each(cb)
    if hasattr(right_node, "right") and right_node.right is not None:
      right_node.right.breadth_first_for_each(cb)
      
    

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
