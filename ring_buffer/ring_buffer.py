class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # check if the buffer has been filled
    if len(self.storage) >= self.capacity:
      self.current = 0 # if so, set current index to 0
    else: 
      self.storage[self.current] = item # otherwise, set current index item equal to passed-in item
      self.current += 1 # then increment to next index
    pass

  def get(self):
    pass