
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity # The capacity of my ring buffer. 
    self.current = 0 # Tracks where I'm appending
    self.storage = [None]*capacity # My initial actual storage object of fixed size. 

  def append(self, item): # Adds elements to the buffer. 
    # One case, add an item to a position
    self.storage[self.current] = item
    self.current = (self.current + 1) % self.capacity # Moves current forward by 1 space, Takes us back to zero if we've cycled through. 

  def get(self): # Returns all of the elements in the buffer, in a list, in their given order.
    return [item for item in self.storage if item] # Returns all real items, i.e. not None. 

