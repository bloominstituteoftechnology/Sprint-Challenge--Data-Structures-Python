class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current % self.capacity] = item
    self.current += 1
    pass

  def get(self):
    if self.current >=self.capacity:
      return self.storage
    else:
      return self.storage[:self.current]


    pass