class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
      self.storage[self.current % len(self.storage)] = item 
      self.current += 1

  def get(self):
      return [x for x in self.storage if x != None] 
