class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    """
    call the anonymous function on each node in the tree 
    this will require a current node variable to reference cb(current.value) for nodes
    for depth-first search we'll traverse the left tree as long as possible
    if this is not possible, go to the previous node
    from previous node, go down the right path until no longer possible, then the left path
    when these paths are complete, go back to previous node again and repeat
    """

    stack = [] # BFS uses stack structures rather than queue
    current = self
    # might need previous node variable, will test without one

    while True:
      cb(current.value)

      if current.right is not None: # add right trees to the stack where applicable
        stack.append(current)
      if current.left is None: # if no more left trees exist and the stack is clear, we are done
        if len(stack) == 0:
          break
        current = stack.pop().right # otherwise, we pop the right value or set it to the left tree if left values exist
      else: current = current.left    

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

# creating a Queue class for use with BFS solution

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, value):
    self.storage.append(value)
    self.size += 1

  def queue(self):
    if self.storage is None:
      return
    self.size -= 1
    return self.storage.pop(0)