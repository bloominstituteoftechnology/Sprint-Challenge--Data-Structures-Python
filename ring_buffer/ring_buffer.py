class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.count = 0

    def _next_idx(self, index):
        return (index + 1) % len(self.storage)


    def append(self, item):
        self.storage[self.head] = item
        self.head = self._next_idx(self.head)
        if self.count < len(self.storage):
            self.count += 1


    def get(self):
        return self.storage[:self.count]