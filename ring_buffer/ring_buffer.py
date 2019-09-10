class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
   self.storage[self.current] = item
   # updates current value to next
   if self.current < self.capacity - 1:
     self.current += 1
   else:
   # goes back to beginning
      self.current = 0
      

  def get(self):
    return [i for i in self.storage if i != None]
