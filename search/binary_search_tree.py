class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    pass
  
  def dequeue(self):
    return self.storage.remove_head()
    pass

  def len(self):
    if self.storage.head is None:
      return 0
    node = self.storage.head
    count = 1
    while node.get_next() is not None:
      node = node.get_next()
      count += 1
    return count
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
    newNode = Node(value)
    if self.head is None:      
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.set_next(newNode)
      self.tail = newNode

    pass

  def remove_head(self):
    if self.head is None:
      return None
    else:
      value = self.head.get_value()
      if self.head is self.tail:
        self.tail = self.head.get_next()
      self.head = self.head.get_next()
      return value

    pass

  def contains(self, value):
    if self.head is None:
      return None

    node = self.head
    while True:
      if node.value is value:
        return True
      if node.get_next() is None:
        return False
      else:
        node = node.get_next()

  def get_max(self):
    node = self.head
    if node is None:
      return None

    value = node.get_value()    
    while node.get_next() is not None:
      node= node.get_next()
      if node.get_value() > value:
        value = node.get_value()
      
    
    return value

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    self.value = cb(self.value)
    if self.left is not None:
      self.left.depth_first_for_each(cb)
    if self.right is not None:
      self.right.depth_first_for_each(cb)
    if self.right is None and self.left is None:
      return
    pass    

  def breadth_first_for_each(self, cb):
    queue = Queue()
    queue.enqueue(self)
    while queue.storage.head:
      node = queue.storage.head.value
      node.value = cb(node.value)      
      if node.left is not None:
        queue.enqueue(node.left)
      if node.right is not None:
        queue.enqueue(node.right)
      queue.dequeue()  
    
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
