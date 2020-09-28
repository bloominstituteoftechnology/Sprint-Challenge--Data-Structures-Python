class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.full = False
        self.storage = []
        self.counter = 0

    def is_full(self, capacity):
        if len(self.storage) > capacity:
            self.full = True

    def append(self, item):
        if not self.full:
            self.storage.append(item)
        else:
            self.storage[self.counter]
            self.counter = (self.counter + 1) % self.capacity
        self.is_full(self.capacity)

    def get(self):
        if self.full:
            return self.storage
        else:
            return [x for x in self.storage if x is not None]