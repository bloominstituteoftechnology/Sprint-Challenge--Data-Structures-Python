class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):

    try:
        self.storage[self.current] = item
        self.current += 1

    except:
      self.current = 0
      self.append(item)
    


  def get(self):
    items = [item for item in self.storage if item != None]
    return items