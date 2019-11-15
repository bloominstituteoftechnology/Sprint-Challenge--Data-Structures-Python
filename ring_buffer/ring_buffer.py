class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # store current item
    self.storage[self.current] = item
    # update counter
    self.current += 1
    # compare counter with capacity
    if self.current == self.capacity:
      self.current = 0


  def get(self):
    # get item if its not None
    return [x for x in self.storage if x is not None]