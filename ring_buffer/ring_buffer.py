class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = -1
        self.storage = []

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.index = (self.index + 1) % self.capacity
            self.storage[self.index] = item
        else:
            self.storage.append(item)
        
    def get(self):
        return self.storage