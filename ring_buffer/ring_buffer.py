class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.cur = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.cur] = item
        else:
            self.storage.append(item)
        self.cur = (self.cur + 1) % self.capacity

    def get(self):
        return self.storage
