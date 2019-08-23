class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
  def append(self, item):  
    # As long as self.current value is less than self.capacity value
    # keep adding the item to the storage
    if self.current < self.capacity:
      self.storage[self.current] = item
      # Increase the count value by 1
      self.current +=1
      #or else...make the self.current value zero then keep adding the items to the storage  
    else:
      self.current = 0
      self.storage[self.current] = item
      self.current +=1

  def get(self):
    arr = []
    for item in self.storage:
      if item != None:
        arr.append(item)
    return arr    
    