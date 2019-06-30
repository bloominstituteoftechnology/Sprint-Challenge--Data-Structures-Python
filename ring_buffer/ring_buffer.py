class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #check to see if current is too large
    #pop old item off end
    #insert new item at currents position
    if self.current >= self.capacity:
      self.current = 0
    self.storage.pop()
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