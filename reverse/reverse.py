class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # test for empty list or has only one node, if list is empty, or had only one node the only option is to return
    if self.head is None or self.head.get_next() is None:
      return
    else:
      # We will use 3 nodes to reverse the list L, C, and R
      # We initially have to start before we start looping
      l = self.head
      c = l.get_next()
      l.set_next(None)
      # Now we loop through while c and c.next exist
      while c and c.get_next():
        r = c.get_next()
        c.set_next(l)
        l = c
        c = r
      # we have to do a final set next on the current, and set the head to our current node
      c.set_next(l)
      self.head = c
