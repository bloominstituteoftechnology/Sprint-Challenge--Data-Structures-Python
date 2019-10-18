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

  # return all elements of cache
  def get(self):
    print(self.storage)
    return [i for i in self.storage if i]


r = RingBuffer(3)
r.append('a')
r.append('b')
r.append('c')
r.append('d')
r.append('e')
r.append('f')
r.append
