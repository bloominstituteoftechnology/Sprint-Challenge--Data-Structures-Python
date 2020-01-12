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

  def __str__(self):
    return str(self.value)

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None
  
  def __str__(self):
    cur_node = self.head
    output = ''
    output += str(cur_node) + ' | '
    if self.head == None:
      output = "Empty"
    else: 
      while cur_node.get_next() is not None:
        cur_node = cur_node.get_next()
        output += str(cur_node) + ' | '
    return output

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
    cur_node = self.head
   
    if cur_node is None:
      return print("Empty")

    # Not sure why this works 
    while cur_node is not None:
      temp_node = cur_node
   
      cur_node = cur_node.next_node

      temp_node.next_node = None

      self.add_to_head(cur_node)

    # Gets rid of self.head = None 
    self.head = self.head.next_node

    return cur_node
    
      
node = LinkedList()
node.add_to_head(1)
node.add_to_head(2)
node.add_to_head(3)


print(node)

node.reverse_list()

print(node)

node.reverse_list()

print(node)
