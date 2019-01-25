class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # Go down the left path until you can't
    # Go back to the previous node and take the right path and then take the left path until you can't
    # Repeat until there are no longer any right paths to take.

    stack = []
    current_node = self

    while True:
      cb(current_node.value)
      if current_node.right is not None:
        stack.append(current_node)
      if current_node.left is None:
        if len(stack) <= 0:
          break
        current_node = stack.pop().right
      else:
        current_node = current_node.left

  def breadth_first_for_each(self, cb):
    pass

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