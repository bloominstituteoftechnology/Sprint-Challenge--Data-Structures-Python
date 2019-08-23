class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    if self.current + 1 > self.capacity - 1:
      self.current = 0
    else:
      self.current += 1

  def get(self):
    low = 0
    high = len(self.storage)-1
    while low <= high:
      middle_index = low + (high - low) // 2
      if self.storage[middle_index] == None:
          high = middle_index - 1
      elif self.storage[middle_index] is not None:
          low = middle_index + 1
    return self.storage[:high + 1]
