class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.rear = -1
    self.front = -1

  def append(self, item):

    if self.current < self.capacity:
      # print("Before: ", self.storage)
      oldest = self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      # print("Current: ", self.current)
      print("After: ", self.storage, "Removed Item: ", oldest)
      self.current = self.current + 1

      if self.current == self.capacity:
        self.current = 0

  def get(self):
    templist = []
    for item in self.storage:
      if item != None:
        templist.append(item)
    return templist
