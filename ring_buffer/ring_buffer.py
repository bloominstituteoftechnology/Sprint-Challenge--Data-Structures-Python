class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # print(self.storage)
    # if self.current <= self.capacity:
    # self.storage.pop(self.current)
    # self.storage.insert(self.current, item)
    self.storage[self.current] = item
    if self.current == len(self.storage) - 1:
      self.current = 0

    else:
      self.current += 1


  def get(self):
    # pass
    return [ i for i in self.storage if i is not None]



# buffer = RingBuffer(5)

# buffer.append(3)