class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass

  def get(self):
    # Create store
    store_list = list(self.storage)
    # check to see if None exists
    i = 0
    for i in store_list:
      # Remove any nones found
      if i is None:
        store_list.remove(None)
    return store_list