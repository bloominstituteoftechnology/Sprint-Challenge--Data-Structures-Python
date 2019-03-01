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
    # Add the current node to the stack
    # Remove the last item from the stack
    # Add the last item's children to the stack

    stack = []
    layer = []
    current_node = self

    while True:
      cb(current_node.value)
      if current_node.left is not None:
        stack.append(current_node.left)
      if current_node.right is not None:
        stack.append(current_node.right)
      if len(stack) <= 0:
        break
      else:
        current_node = stack.pop(0)

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