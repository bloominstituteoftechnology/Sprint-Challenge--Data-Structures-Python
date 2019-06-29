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
    self.storage[self.current] = item
    # Increment the value we're currently inserting at
    self.current += 1
    # If we're now trying to insert outside of the capacity
    # of our storage reset it.
    if (self.current >= self.capacity): 
      self.current = 0

  def get(self):
    pass

myRingBuffer = RingBuffer(3)
myRingBuffer.append(5)
myRingBuffer.append(6)
myRingBuffer.append(8)
myRingBuffer.append(9)
myRingBuffer.append(1)
myRingBuffer.append(3)
print(myRingBuffer.storage)