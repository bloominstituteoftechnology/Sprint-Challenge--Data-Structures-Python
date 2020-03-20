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
    
    # TO BE COMPLETED
    #can only move one direction...forward
    #start at the beginning, make the head the tail, the tail becomes the head 
    # set next number to be next.previous because they need to connect 
    #passing all tests!
    
    # steps:
    #   create prev position, current position, and next position variables 
    #   using loop to iterate through the list while it is not empty 
    #   store current next node in variable
    #   then store previous position in the current next 
    #   then current becomes previous and previous becomes next 
    #   the head becomes previous 
    
    #start off with no previous and the current position at head 
    prev_position = None
    current_position = self.head 
    
    #while not empty...do pseudo above 
    while current_position is not None:
      next_position = current_position.next_node
      current_position.next_node = prev_position
      
      #moving through the list 
      prev_position = current_position
      current_position = next_position
      
    self.head = prev_position
      
      

   
      
    
    
    

