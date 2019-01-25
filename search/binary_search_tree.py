class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    
    """
    The basic algorithm of Pre-order traversal is to visit the root, traverse the left subtree, then traverse the right subtree.
    Here, we're going to check the left or right, and recursively call the depth_first method, while passing in cb.
    cb is the closure (lambda in Python) that will hold on to the value so it can be used in the test file.
    """
    
    # Calling the callback with the current parent
    cb(self.value)
    
    # Traverse the left side
    if self.left is not None:
      self.left.depth_first_for_each(cb)
    
    if self.right is not None:
      self.right.depth_first_for_each(cb)
    

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
