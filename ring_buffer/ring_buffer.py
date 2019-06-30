class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # Keep adding the item to the storage
        # if current value is less than capacity value
        if self.current < self.capacity:
            self.storage[self.current] = item
        # Increase the count value by 1
            self.current += 1
        # If current value is greater than capacity
        # reset current value zero and 
        # then keep adding the items to the storage
        else:
            self.current = 0
            self.storage[self.current] = item
            self.current += 1

    def get(self):
      pass