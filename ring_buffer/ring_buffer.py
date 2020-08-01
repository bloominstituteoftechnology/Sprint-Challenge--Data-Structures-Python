class RingBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity
        self.position = 0

    def append(self, item):
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
            self.position += 1
        else:
            self.buffer[self.position] = item
            self.position += 1

        if self.position >= self.capacity:
            self.position = 0

    def get(self):
        return self.buffer