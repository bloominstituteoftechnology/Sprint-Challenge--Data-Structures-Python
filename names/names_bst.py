class BSTNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def insert(self, value):
    if value < self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BSTNode(value)
    else:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BSTNode(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value and self.left:
      return self.left.contains(target)
    elif target > self.value and self.right:
      return self.right.contains(target)