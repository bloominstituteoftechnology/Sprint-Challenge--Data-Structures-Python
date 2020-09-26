class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.curr = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.curr] = item
            self.curr = (self.curr + 1) % self.capacity
        else:
            self.storage.append(item)    

    def get(self):
        return self.storage