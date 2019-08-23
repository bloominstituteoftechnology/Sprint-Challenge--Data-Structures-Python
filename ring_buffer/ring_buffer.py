class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
   self.storage.pop(self.current)
   self.storage.insert(self.current, item)
   if self.current == len(self.storage) - 1:
     self.current = 0 
   else:
     self.current += 1
    

  def get(self):
    return [n for n in self.storage if n is not None]