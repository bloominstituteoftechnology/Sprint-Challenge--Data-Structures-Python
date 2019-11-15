class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    
    if self.current >= self.capacity:
      # overright the last element with the first
      self.current += 1
      index = (self.current % self.capacity) -1
      self.storage[index] = item
    
    else:
      # base case
      self.current += 1
      index = (self.current) -1
      self.storage[index] = item


  def get(self):
    return [x for x in self.storage if x is not None]