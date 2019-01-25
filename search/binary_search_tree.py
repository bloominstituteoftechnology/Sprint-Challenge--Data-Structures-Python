class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  def breadth_first_for_each(self, cb):
    left_tree = BinarySearchTree(self.left)
    left_mega_tree = BinarySearchTree(self.left.left)
    right_tree = BinarySearchTree(self.right)
    right_mega_tree = BinarySearchTree(self.right.right)
    if self.value is None:
        return cb(None)
    if not self.left:
      return cb(self.value)
      print("What", self.value)
    if self.value:
      cb(self.value)
      print("4??",self.value)
    if self.left:
        cb(self.left.value)
        # self.left = left_tree
        print("4??",self.left.value)
    if self.right:
        cb(self.right.value)
        
        print("is it 4:::", self.right.value)
    if self.left.left:
        print("is it 4###", self.value)
        # cb(self.left.right.value)
    if self.left.right:
        print("is it 4!?!?!", self.left.right.value)
        self.right = right_tree
        # self.left = left_tree
        cb(self.left.right.value)
        print(self.right)

    if self.right.left:
        self.left = left_tree
        cb(self.right.left.value)
        print("is it???",self.right.left.value)
    if self.right.right:
        cb(self.right.right.value)
        # self.right.right = right_mega_tree
        print("is it???",self.right.value)
    
    
    


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
