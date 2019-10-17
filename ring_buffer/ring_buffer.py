class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # print(self.storage)
    # if self.current <= self.capacity:
    # self.storage.pop(self.current)
    # self.storage.insert(self.current, item)

        # tried doing a pop and insert method but i realized that might be too dangerous and if something breaks inbetween then the the origional element is lost and might loop to never reaching the capactiy.  So i used an assignment line instead and boggled it down to one line of code rather then two

    self.storage[self.current] = item
    if self.current == len(self.storage) - 1:
      self.current = 0

    else:
      self.current += 1


  def get(self):
    # pass
    return [ i for i in self.storage if i is not None]



# buffer = RingBuffer(5)

# buffer.append(3)