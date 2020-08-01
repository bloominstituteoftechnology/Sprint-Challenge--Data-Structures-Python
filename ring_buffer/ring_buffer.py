class RingBuffer:
    def __init__(self, capacity):

        """constructor function for the RingBuffer class."""
        self.capacity = capacity
        self.storage = []
        self.mod_index = 0

    def append(self, item):

        """adds the item to internal storage, and overwrites oldest items if over capacity."""
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.mod_index] = item
            self.mod_index = ((self.mod_index + 1) % self.capacity)
            

    def get(self):
        
        """return the stored items."""
        return self.storage