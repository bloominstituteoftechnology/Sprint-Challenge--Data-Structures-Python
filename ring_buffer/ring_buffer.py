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
    return [index for index in self.storage if index != None]