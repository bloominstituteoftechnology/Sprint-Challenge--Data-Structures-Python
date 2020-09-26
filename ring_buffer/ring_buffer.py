class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = -1
        self.buffer = []

    def append(self, item):
        if len(self.buffer) == self.capacity:
            self.current = (self.current + 1) % self.capacity
            self.buffer[self.current] = item
        else:
            self.buffer.append(item)

    def get(self):
        return self.buffer