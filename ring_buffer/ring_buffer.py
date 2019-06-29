class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
# The `append` method adds elements to the buffer.

    # Change value at self.current to the item's value
      self.storage[self.current] = item
    # increment self.current
      self.current += 1

    # When self.current is the same as self.capacity reset self.current
      if self.current == self.capacity:
        self.current = 0

  def get(self):
# The `get` method returns all of the elements in the buffer in a list in their given order. 
# It should not return any `None` values in the list even if they are present in the ring buffer.
    return [ i for i in self.storage if i != None]