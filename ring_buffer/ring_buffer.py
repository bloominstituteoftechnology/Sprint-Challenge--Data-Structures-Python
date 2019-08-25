class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #check to see if current is too large if so reset to 0
    if self.current >= self.capacity:
      self.current = 0
    self.storage.remove(self.storage[self.current])
    self.storage.insert(self.current, item)
    self.current +=1

  def get(self):
    #only return if not none
    return [item for item in self.storage if item != None]

buffer = RingBuffer(3)
print(buffer.get())

buffer.append("a")
buffer.append("b")
buffer.append("c")

print(buffer.get())

buffer.append("d")

print(buffer.get())