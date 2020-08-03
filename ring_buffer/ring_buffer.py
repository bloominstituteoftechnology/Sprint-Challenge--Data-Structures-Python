class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        self.storage.append(item)
        if len(self.storage) == self.capacity:
            self.current = 0
            self.__class__ = FullBuffer

    def get(self):
        return self.storage
    

class FullBuffer(RingBuffer):
    def __init__(self, capacity, storage):
        super().__init__(capacity)
    def append(self, item):
        self.storage[self.current] = item
        self.current = (self.current+1) % self.capacity
    def get(self):
        return self.storage