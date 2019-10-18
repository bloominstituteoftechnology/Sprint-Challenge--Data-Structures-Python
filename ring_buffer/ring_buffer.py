class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    li = []
    for i in self.storage:
      if i:
        li.append(i)
    return li