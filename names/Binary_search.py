class BinarySearch:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
        if not self.left:
            self.left = BinarySearchTree(value)
            
        else:
            self.left.insert(value)

    if value >= self.value:
        if not self.right:
            self.right = BinarySearchTree(value)

        else:
            self.right.insert(value)


  def contains(self, target):
  
    if self.value == target:
        return True

    if self.value > target and self.left:
        if self.left.contains(target):
            return True

    elif self.value < target and self.right:
        if self.right.contains(target):
            return True

    else:
        return False


  def get_max(self):
    if self.right is None:
        return self.value

    else:
        return self.right.get_max()


  def for_each(self, cb):
    cb(self.value)

    if self.right:
        self.right.for_each(cb)

    if self.left:
        self.left.for_each(cb)