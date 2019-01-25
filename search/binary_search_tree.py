class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    if self.left == None and self.right == None:
      return cb(self.value)
    
    cb(self.value)

    def recursed_left(tree):
      cb(tree.value)
      if tree.left == None and tree.right != None:
        cb(tree.right.value)
        return
      recursed_left(tree.left)

    def recursed_right(tree):
      cb(tree.value)
      if tree.left == None and tree.right == None:
        return
      recursed_right(tree.right)

    recursed_left(self.left)
    recursed_right(self.right)

  def breadth_first_for_each(self, cb):
    if self.left == None and self.right == None:
      return cb(self.value)

    arr = []
    arr.append(self.value)

    def tree(ll):
      if ll == None:
        return
      if ll.left != None:
        arr.append(ll.left.value)
      if ll.right != None:
        arr.append(ll.right.value)
      tree(ll.left)
      tree(ll.right)

    tree(self)
    
    for i in arr:
      cb(i)
  

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
