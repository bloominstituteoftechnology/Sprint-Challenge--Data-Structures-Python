class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage.pop(self.current)
    self.storage.insert(self.current, item)

    if self.current == len(self.storage ) - 1:
      self.current = 0

    else:

        self.current += 1


  def get(self):
    # make sure you are not returning none
    # iterate through array
     return [x for x in self.storage if x is not None]


    # arr = []
    # if None in self.storage:
    #   for x in self.storage:
    #    if x != None:
    #     arr.append(x)

    # return arr


#Keep this in mind
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']