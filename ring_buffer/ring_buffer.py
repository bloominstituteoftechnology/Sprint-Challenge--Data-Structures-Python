class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current > (self.capacity -1):
      self.current = 0
      self.storage[self.current] = item
      self.current +=1
    else:
      self.storage[self.current] = item
      self.current +=1

  def get(self):
    # Return if not None
    return [item for item in self.storage if item != None]