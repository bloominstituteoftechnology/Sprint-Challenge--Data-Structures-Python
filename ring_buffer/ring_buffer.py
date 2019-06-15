class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == self.capacity:
      self.current = 0
    if self.storage[self.current] is None:
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1
    else:  
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1    
    
  def get(self):
    x = 0
    new_list = list(self.storage)
    for x in new_list:
      if x is None:
        new_list.remove(None)
    
    for x in new_list:
      if x is None:
        new_list.remove(None) 
    
    return new_list
    
 

