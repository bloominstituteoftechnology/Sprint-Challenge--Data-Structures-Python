class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    stack = [self]

    while len(stack):
        node = stack.pop()
        cb(node.value)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)  

  def breadth_first_for_each(self, cb):
    queue = [self]

    while len(queue):
        node = queue.pop(0)
        cb(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

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
