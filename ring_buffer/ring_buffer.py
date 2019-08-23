class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    if self.current == self.capacity - 1:
      self.current = 0
    else:
      self.current += 1

  def get(self):
    if self.storage[-1] == None:
      return self.storage[:self.current]
    else:
      return self.storage