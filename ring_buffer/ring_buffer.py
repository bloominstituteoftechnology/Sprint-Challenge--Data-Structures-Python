class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if None in self.storage:
      x = self.storage.index(None) 
      self.storage[x] = item
      self.current = x
    else :
      if self.current == self.capacity-1:
        x = abs(self.current - (self.capacity-1))
        self.storage[x] = item
        self.current = x
      else: 
        x = self.current+1
        self.storage[x] = item
        self.current = x 
    pass

  def get(self):
    tempList = []
    if None in self.storage:
      for x in self.storage:
        if x != None:
          tempList.append(x)
      return tempList
    else: 
      return self.storage
    pass