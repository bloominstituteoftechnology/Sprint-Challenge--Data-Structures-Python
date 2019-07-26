class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1
    else:
      self.current = 0
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1

    
    # r = self.storage
    # if not item: 
    #   return
    # else:
    #   r.append(item)
    #   del r[0]
    #   return r


  def get(self):
    r = []
    for i in range(self.capacity):
      if self.storage[i] != None:
        r.append(self.storage[i])
    return r
    
    
    
    # r = []
    # for i in range(len(self.storage) -1):
    #   if i is not None:
    #     r.append(self.storage[i])
    # return r