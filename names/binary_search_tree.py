class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    
    if value >= self.value:
      if self.right:
        return self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)
    else:
      if self.left:
        return self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)

  def contains(self, target):
    
    if self.value == target:
      return True

    if self.value > target:
      if self.left:
        return self.left.contains(target)
      else:
        return False

    elif self.value < target:
      if self.right:
        return self.right.contains(target)
      else:
        return False

    else:
      return False

  def get_max(self):
  
    max = self.value
    right_property = self.right

    while right_property:
      if right_property.value > max:
        max = right_property.value

      if right_property.right:
        right_property = right_property.right
      else:
        right_property = None

    return max

  def for_each(self, cb):

    cb(self.value)

    if self.right:
      self.right.for_each(cb)

    if self.left:
      self.left.for_each(cb)