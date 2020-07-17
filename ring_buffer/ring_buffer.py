class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [] * capacity
        self.index = 0


    def append(self, item):
        if len(self.storage) is not self.capacity:
             self.storage.append(item)
        else:
            self.storage[self.index] = item 
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return self.storage