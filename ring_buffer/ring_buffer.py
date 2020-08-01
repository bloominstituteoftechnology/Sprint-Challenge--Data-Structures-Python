class RingBuffer:
    def __init__(self, capacity):
        buffer = []
        self.head = 0
        self.capacity = capacity
        self.buffer = list(buffer)[-capacity:]

    def append(self, item):
        if len(self.buffer) == self.capacity:
            self.buffer[self.head] = item
        else:
            self.buffer.append(item)
        self.head = (self.head + 1) % self.capacity

    def get(self):
        return self.buffer