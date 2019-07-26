class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # print(self.storage)
    if None in self.storage:
      # print(self.storage)
      # print(self.capacity)
      self.storage.pop(0)
      # print(self.storage)
      # print(self.capacity)
      self.storage.append(item)
      # print(self.storage)
      # print(self.capacity)
    elif self.current < self.capacity:
      self.storage[self.current - self.capacity] = item
      self.current += 1
      # print(self.storage)
      # print(self.capacity)
      # print(self.current)
    # technically another else statement here if self.current = self.capacity
    # set self.current to 0 and recursion

  def get(self):
    arr = []
    for x in self.storage:
      # print(self.storage)
      if x != None:
        # print(self.storage)
        arr.append(x)
      elif self.storage == [None]*self.capacity:
        return []
    return arr



# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']