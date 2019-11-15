class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current > self.capacity - 1:
      self.current = 0
    self.storage[self.current] = item
    self.current += 1

  def get(self):
    temp = []
    for i in self.storage:
      if i != None:
        temp.append(i)
    return temp
