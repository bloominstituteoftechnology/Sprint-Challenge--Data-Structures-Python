# Created by Ben Hakes

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    self.current = self.current % len(self.storage)

  def get(self):
    array_to_return = []
    for index in self.storage:
      if index != None:
        array_to_return.append(index)
    return array_to_return 