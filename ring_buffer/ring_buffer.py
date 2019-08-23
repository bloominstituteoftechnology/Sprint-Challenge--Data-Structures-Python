class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  

  def append(self, item):
# self.current is the newest element. Old is characterized by an element to
# to the right of self.current or if the end of the array the first element in
# the array
    if len(self.storage) < self.current:
      self.current = 0
    
    
    # should take care of all None's
    # if self.storage[self.current]
    try:
      value = self.storage[self.current]
    except IndexError:
      self.current = 0
    
    if self.storage[self.current] == None:
      self.storage[self.current] = item
      self.current += 1
      
    else:
      if self.current == 0:
        self.storage[0] = item
        self.current += 1
      elif self.current >= len(self.storage):
        self.storage[0] = item
      else:
        self.storage[self.current] = item
        self.current += 1

    print(self.storage)

# how to implement oldest element is removed?
  

    pass

  def get(self):
    tempArr = []
    for i in range(len(self.storage)):
      if self.storage[i] != None:
        tempArr.append(self.storage[i])
        # self.storage.pop(i)

    return print(tempArr)
    # pass


buffer = RingBuffer(3)
buffer.get()
buffer.append(1)
buffer.append(2)
buffer.get()
buffer.append(3)
buffer.append(4)
buffer.append(5)
buffer.append(6)
buffer.append(7)
buffer.append(8)
