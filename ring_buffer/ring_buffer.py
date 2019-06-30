# RingBuffer needs to send back any non-None values.
# Appending to RingBuffer fills up its capacity first
# and then restarts at the first index overwriting values

# I can use the current variable to maintain what index
# we can currently assign values to. And if it is greater
# than the capacity reset it to 0
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # Add the value
    self.storage[self.current] = item #O(1)
    # Increment the value we're currently inserting at
    self.current += 1 #O(1)
    # If we're now trying to insert outside of the capacity
    # of our storage reset it.
    if (self.current >= self.capacity): #O(1)
      self.current = 0 #O(1)

  def get(self):
    retBuffer = []
    # Looping through the entire storage array so this is O(n)
    for item in self.storage: #O(n)
      if item is not None:
        retBuffer.append(item)
    return retBuffer

myRingBuffer = RingBuffer(3)
myRingBuffer.append(5)
myRingBuffer.append(6)
myRingBuffer.append(8)
myRingBuffer.append(9)
myRingBuffer.append(1)
myRingBuffer.append(None)
print(myRingBuffer.storage)
print(myRingBuffer.get())