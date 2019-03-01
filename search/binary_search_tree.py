class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    visited=[]
    def helper (node, cb):
      nonlocal visited  
      if node.left:
        cb(node.value)
        visited.append(node)
        helper(node.left,cb)
      if node.right:
        if node not in visited:
            cb(node.value)
        helper(node.right,cb)
      if not node.right and not node.left:
        cb(node.value)
    helper(self,cb)


  def breadth_first_for_each(self, cb):
    visited=[]
    cb(self.value)
    def helper (node, cb):
        nonlocal visited
        current_node=node
        if node.left is not None:
          cb(node.left.value)
          visited.append(node.left)
          cb(node.right.value)
          visited.append(node.right)
          helper(current_node.left,cb)
        if node.right is not None:
          if node.right not in visited:
            cb(node.right.value)
          helper(current_node.right,cb) 
    helper(self, cb)

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
