# When the ring buffer is full, but we need to add a new element...
# The oldest element in the ring buffer is overwritten with the newest element. 
# This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  # Adds elements to the buffer 
  def append(self, item):
    pass

  # Returns all elements in their given order, but should not return None values 
  def get(self):
    pass