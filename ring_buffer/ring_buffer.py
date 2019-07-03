class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #if we are past last index, reset to beginning
    if self.current > self.capacity:
      self.current = 0
    #sets storage to new incoming item  
    self.storage[self.current] = item
    #increases index
    self.current += 1
    print(self.storage)  

  def get(self):
    print([i for i in self.storage if i != None])
    return [i for i in self.storage if i != None]

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']    