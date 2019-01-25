from queue import Queue
from stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    stack = Stack()
    stack.push(self)

    while stack.size() > 0:
        node = stack.pop()
        cb(node.value)

        if node.right is not None:
            stack.push(node.right)

        if node.left is not None:
            stack.push(node.left)  

  def breadth_first_for_each(self, cb):
    queue = Queue()
    queue.enqueue(self)

    while queue.len() > 0:
        node = queue.dequeue()
        cb(node.value)

        if node.left is not None:
            queue.enqueue(node.left)

        if node.right is not None:
            queue.enqueue(node.right)

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
