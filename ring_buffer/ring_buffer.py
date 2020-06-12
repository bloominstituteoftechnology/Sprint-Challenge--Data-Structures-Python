class RingBuffer:
    def __init__(self, capacity):
        self.index = 0
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        if len(self.buffer) == self.capacity:
            self.buffer[self.index] = item
        else:
            self.buffer.append(item)
        self.index = (self.index + 1) % self.capacity
        
    def get(self):
        return self.buffer