class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


  def depth_first_for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.depth_first_for_each(cb)
    if self.right:
      self.right.depth_first_for_each(cb)


  def breadth_first_for_each(self, cb):
    queue = Queue()
    queue.enqueue(self)
    # print('1', queue.size)
    while queue.size != 0:
      print(queue.size)
      self = queue.dequeue()
      cb(self.value)
      if self.left:
        queue.enqueue(self.left)
      if self.right:
        queue.enqueue(self.right)

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

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    if self.storage.head is None:
      self.size = 0
      return None
    else:
      self.size -= 1
      return self.storage.remove_head()

  def len(self):
    return self.size

class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    # new_node.next_node = None
    if self.head is None and self.tail is None:
      self.head = self.tail = new_node
      # self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = self.tail.next_node

  def remove_head(self):
    old_head = self.head
    if old_head is None: # Empty Linked List
      return None
    elif old_head == self.tail:  # Only 1 val in Linked List
      self.head = None
      self.tail = None
      return old_head.get_value()
    else:                     # Two or more vals in Linked List
      self.head = self.head.get_next()
      return old_head.get_value()



  def contains(self, value):
    current = self.head
    while current:
      if current.get_value() == value:
        return True
      else:
        current = current.get_next()
    return False

  def get_max(self):
    current = self.head
    if current is None:
      return None
    max_node = current
    next_up = current.get_next()
    while next_up:
      if next_up.get_value() > max_node.get_value():
        max_node = next_up
      else:
        next_up = next_up.get_next()
    return max_node.get_value()