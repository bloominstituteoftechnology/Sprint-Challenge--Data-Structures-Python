class RingBuffer:
    def __init__(self, capacity):
        self.buffer = [] * capacity
        self.capacity = capacity - 1 # Minus 1 to account for 0 indexing
        self.position = 0

    def append(self, item):
        self.buffer[self.position] = item
        self.position += 1

        if self.position >= self.capacity:
            self.position = 0

    def get(self):
        return self.buffer