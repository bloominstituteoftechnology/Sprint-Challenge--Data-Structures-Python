class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.full = False

    def append(self, item):
        if self.full:
            self.storage[self.oldest_index] = item
            self.oldest_index = (self.oldest_index+1) % self.capacity
        else:
            self.storage.append(item)
            if len(self.storage) == self.capacity:
                self.full = True
                self.oldest_index = 0

    def get(self):
        return self.storage

