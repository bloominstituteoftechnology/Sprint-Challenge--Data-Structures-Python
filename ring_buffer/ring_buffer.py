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
    self.storage[current] = item
    # Increment the value we're currently inserting at
    self.current += 1
    # If we're now trying to insert outside of the capacity
    # of our storage reset it.
    if (self.current > self.capacity): 
      self.current = 0
    pass

  def get(self):
    pass