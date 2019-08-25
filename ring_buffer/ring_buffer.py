class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current >= self.capacity:
      self.current = 0
    self.storage[self.current] = item
    self.current +=1
      

  def get(self):
    return  [item for item in self.storage if item != None]

buffer = RingBuffer(5)
buffer.append('a')
print(buffer.get())
buffer.append('b')
print(buffer.get())
buffer.append('c')
print(buffer.get())
buffer.append('d')
print(buffer.get())
buffer.append('e')
print(buffer.get())
buffer.append('f')
print(buffer.get())
buffer.append('g')
buffer.append('h')
buffer.append('i')
print(buffer.get())