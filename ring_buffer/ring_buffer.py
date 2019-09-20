class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    #if ring buffer is full (available capacity is 0), this adds an element to the array and sets current to the first index
    if self.current == self.capacity - 1:
      self.current = 0
    #if ring buffer is not full, adds element to this array
    elif self.current < self.capacity - 1:
      self.current += 1

  def get(self):
    print([item for item in self.storage if item is not None])
    
    