import os
import sys
#sys.path.append('../ring_buffer')
#sys.path.append(".")
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.holding = DoublyLinkedList()
    self.oldest = None
    self.newest = None
    self.next = None
    self.prev = None
    self.replacedHead = False
  #self.tail = (self.tail + 1) % self.capacity

  def append(self, item):
    if len(self.holding) == self.capacity:

      if self.holding.head is not None:
        self.prev.value = item
        self.prev = self.prev.next


    else:
      self.next = self.holding.head
      self.prev = self.next
      self.holding.add_to_tail(item)

  """
  passes 8/9 tests
    if len(self.holding) == self.capacity:

      if self.holding.head is not None:
        #next = self.holding.head.next
        self.holding.remove_from_head()
        self.holding.add_to_head(item)


    else:
      self.holding.add_to_tail(item)


"""
  def get(self):
    """
    current2 = self.holding.head
    if (self.holding.head == None):
      print("List is empty");
      return
    print("Nodes of doubly linked list: ")
    while (current2 != None):
      # Prints each node by incrementing pointer.
      print(current2.value),
      current2 = current2.next
      """
    values = []
    temp = self.holding.head
    while temp is not None:
      values.append(temp.value)
      temp = temp.next

    return values
    #return values[::-1]