class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage = [i for i in self.storage if i is not None]
    if len(self.storage) == self.capacity:
      self.storage[self.current] = item
      self.current = (self.current + 1) % self.capacity

    if len(self.storage) != self.capacity:
      self.storage.append(item)

      while len(self.storage) < self.capacity:
        self.storage.insert(len(self.storage), None)

  def get(self):
    self.storage = [i for i in self.storage if i is not None]
    return self.storage