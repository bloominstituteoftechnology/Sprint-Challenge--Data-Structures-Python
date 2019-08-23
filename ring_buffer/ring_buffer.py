class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0  # holds oldest value index
    self.storage = [None]*capacity

  def append(self, item):
    if self.capacity > len(self.storage):
      self.storage.append(item)
      self.current += 1
    else:
      self.storage[self.current] = item
      self.current = ((self.current + 1) % self.capacity) 

  def get(self):
    values = []
    for x in self.storage:
      if x is not None:
        values.append(x)
    return values


buff = RingBuffer(5)
buff.append(0)
buff.append(1)
buff.append(2)
buff.append(3)
buff.append(4)
buff.append(5)
buff.append(6)
print(buff.get())