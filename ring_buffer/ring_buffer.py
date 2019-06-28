class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item

    if self.current < self.capacity - 1:
    	self.current += 1
    else:
    	self.current = 0

  def get(self):
    filtered_list = []

    for el in self.storage:
    	if el:
    		filtered_list.append(el)

    return filtered_list