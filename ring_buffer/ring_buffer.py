class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        self.data.append(item) 
        if len(self.data) == self.capacity: 
            self.counter = 0
            self.__class__ = self.CapacityMax

    def get(self):
        return self.data

    class CapacityMax: 
        def append(self, item): 
            self.data[self.counter] = item
            self.counter = (self.counter + 1) % self.capacity

        def get(self): 
            return self.data