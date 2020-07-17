class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0 # pointer for the buffer

    def append(self, item):
        # capacity must be positive
        if self.capacity > 0:
            # pointer within capcity, point to next 
            if self.current < self.capacity:
                self.storage[self.current] = item
                self.current += 1
            # pointer exceeds capacity, point back to start
            elif self.current == self.capacity:
                self.current = 0
                self.storage[self.current] = item
                self.current += 1
        else:
            return None
            
    def get(self):
        storage_none_removed = []
        for i in self.storage:
            if i:
                storage_none_removed.append(i)
        return storage_none_removed