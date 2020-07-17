class RingBuffer:
    def __init__(self, capacity, store=[]):
        self.index = 0
        self.capacity = capacity
        self.store = list(store)[capacity:]


    def append(self, item):
        if len(self.store) == self.capacity:
            self.store[self.index] = item
        else:
            self.store.append(item)
        self.index = (self.index + 1) % self.capacity


    def get(self):
        return(self.store)