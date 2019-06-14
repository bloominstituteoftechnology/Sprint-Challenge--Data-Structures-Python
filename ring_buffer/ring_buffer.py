class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
      # This storage is filled with None at the beginning. The first thing I need to do is check to see if the list contains None. If so, I replace the first instance of None with the item.
    if None in self.storage:
        first_instance = self.storage.index(None)
        self.storage[first_instance] = item
    else:
        self.storage[self.current] = item
        if self.current < self.capacity - 1:
            self.current += 1
        else:
            self.current = 0
  def get(self):
    return_value = [i for i in self.storage if i != None]
    return return_value
