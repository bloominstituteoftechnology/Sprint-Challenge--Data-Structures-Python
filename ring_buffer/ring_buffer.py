
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
        self.storage[self.current] =  value
        self.current +=1
    else:
        self.current = 0
        self.storage[self.current] = value
        self.current +=1


  def get(self):
    return [i for i in self.storage if i != None]
