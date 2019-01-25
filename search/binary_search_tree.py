import sys
#need import os?

# sys.path.append('../linked_list')
# from linked_list import LinkedList

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

  #first create new node
  def add_to_tail(self, value): #could also add value arg but dont need to.
    #create new node
    node = Node(value)
    #set tail of existing tail to next new node
    #cant set tail if none. if LL not empty set tail to new node. if empty set new node to head.
    if self.tail is not None:
        self.tail.set_next(node)
    else: 
        self.head = node
    #set LL tail to new node
    self.tail = node

  def remove_head(self):
      #check if head is none
      #set head node's next node value to a temp val
    if self.head is not None:
      #store value to be returned
      old_head = self.head.get_value()
      #assign new head
      new_head = self.head.next_node
      #if there is another item
      if new_head is not None:
        self.head = new_head
      else: 
        self.head = None
        self.tail = None
      return old_head
      
  def contains(self, value):
    #set current node to head. if node is null return false. 
    # elif node value matches query value return true. else set current node to tail.
    curr_node = self.head

    #while current node exists
    while curr_node:
      #if current node is equal to target value return true
      if curr_node.get_value() == value:
        return True
      #proceed to next node
      curr_node = curr_node.next_node
    #if value not in list
    return False

  def get_max(self):
    #if head is none return none
    if self.head is None:
      return None
    #set head as max value (temp val)  
    max_val = self.head.get_value()
    curr_node = self.head
    # step through each node and compare and if it's bigger set that as max.
    while curr_node is not None:
      if curr_node.get_value() > max_val:
        max_val = curr_node.get_value()
      curr_node = curr_node.get_next()
    #then return the value
    return max_val

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  #add elements to queue FIFO so add to tail
  def enqueue(self, item):
      self.storage.add_to_tail(item)
      self.size += 1

  #remove head
  def dequeue(self):
    if self.storage.head is None: 
      return None
    #need to increment or decrement before return statement
    #return item removed
    else:
      self.size -= 1
      return self.storage.remove_head()
   
  def len(self):
    return self.size


class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass

  #anonymous function is called on every node in correct order
  def breadth_first_for_each(self, cb):
    queue =[]
    queue.append(self)
    #while queue exists
    while queue:
      #FIFO removal from queue
      current_node = queue.pop(0) #0? empty?
      #callback
      cb(current_node.value)
      #add to queue
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)



    

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
