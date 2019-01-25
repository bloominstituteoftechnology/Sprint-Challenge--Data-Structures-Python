class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  def breadth_first_for_each(self, cb):
    left_tree = BinarySearchTree(self.left)
    right_tree = BinarySearchTree(self.right)
    if self.value is None:
        return cb(None)
    if not self.left:
      return cb(self.value)
    if self.value:
      cb(self.value)
    if self.left:
        cb(self.left.value)
    if self.right:
        cb(self.right.value)
        self.left = left_tree
        print("is it 4", self.value)
    if self.left.left:
        print("is it 4", self.value)
        cb(self.left.right.value)
    if self.left.right:
        print("is it 4", self.left.right)
        cb(self.left.right.value)
        self.right = right_tree
    if self.right.left:
        cb(self.right.left.value)
    if self.right.right:
        cb(self.right.right.value)
    
    
    


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
