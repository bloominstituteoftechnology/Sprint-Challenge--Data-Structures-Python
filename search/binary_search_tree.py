class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # invokes cb which adds to arr in test
    cb(self.value)
    # recursively invoke depth_first search_for_each() on the left
    if self.left:
      self.left.depth_first_for_each(cb)
    # recursively invoke depth_first search_for_each on the right
    if self.right:
      self.right.depth_first_for_each(cb)
  '''
  Instructor Pseudo Code:
    - mark node as visited by valling 'cb'
    - if left is not None, call DFS on left
      - self.left.depth_first_for_each(cb)
    - if left is not None, call DFS on left
      - self.right.depth_first_for_each(cb)

  Instructor Second Pseudo Code:
    - create empty stack
    - push root node to the stack
    - while stack is not empty
      - pop the firt item in the stack
      - mark node as visited by calling 'cb'
      - if left is not None, put the left chld in the stack
      - if right is not None, put the right chld in the stack
  '''
    

  def breadth_first_for_each(self, cb):
    # start value
    queue = [self]
    # checking that queue is not empty
    while queue:
      # removes first value in queue and stores it in curr_node
      curr_node = queue.pop(0)
      # invokes cb which adds to arr in test
      cb(curr_node.value)
      # checks left node value and if it exist it gets added to queue
      if curr_node.left:
        queue.append(curr_node.left)
      # checks right node value and if it exist it gets added to queue
      if curr_node.right:
        queue.append(curr_node.right)
  '''
  Instructor Pseudo Code:
    - create empty queue
    - add root node to the queue
    - while queue is not empty
      - dequeue the firt item in the queue
      - mark node as visited by calling 'cb'
      - if left is not None, put the left chld in the queue
      - if right is not None, put the right chld in the queue
  '''

    


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
