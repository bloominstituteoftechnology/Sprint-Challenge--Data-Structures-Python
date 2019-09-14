class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    print('passed in item: ' + item)
    print('current index: ')
    print(self.current)
    # check if the buffer has been filled
    if self.current > self.capacity-1:
      self.current = 0 # if so, set current index to 0
      self.storage[self.current] = item # overwrite existing item
      self.current +=1 # increment index by 1
    else:
      self.storage[self.current] = item # otherwise, set current index item equal to passed-in item
      self.current += 1 # then increment to next index
    print('current storage: ')
    print(self.storage)

  def get(self):
    # create a placeholder variable as an empty list
    newList = []
    # iterate current storage
    for i in range(self.capacity): # append item to the placeholder if != None
      if self.storage[i] != None:
        newList.append(self.storage[i])
    return newList