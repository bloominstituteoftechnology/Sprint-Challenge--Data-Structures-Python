class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # check the current index
    if self.current == self.capacity:
      # reset current index to zero
      self.current = 0
    # overwrite current array element
    self.storage[self.current] = item
    # increment current
    self.current += 1

  def get(self):
    # init empty array
    result = []
    # iterate thru array
    for i in range(self.capacity):
      # check if item is == None
      if self.storage[i]:
        result += self.storage[i]
    # return array
    return result

"""
buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.get())
print(buffer.storage)
buffer.append('e')
print(buffer.get())
"""