class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None for i in range(capacity)]

    def append(self, item):
        if self.capacity == self.size:
            self.data[0] = item
            self.size = 1
        else:
            self.data[self.size] = item
            self.size += 1

    def get(self):
        if self.size > 0:
            return [i for i in self.data if i is not None]
