class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = []
    self.count = 0

  def append(self, item):
    if not self.storage:
      [self.storage.append(None) for _ in range(self.capacity)]
    if self.count + 1 > self.capacity:
      self.count = 0
    self.storage[self.count] = item
    self.count += 1

  def get(self):
    items = [item for item in self.storage if item is not None]
    return items