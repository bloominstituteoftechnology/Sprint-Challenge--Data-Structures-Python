class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            
        elif len(self.storage) == self.capacity:            
            self.storage[self.current] = item
            self.current = (self.current + 1) % self.capacity


    def get(self):
        return self.storage