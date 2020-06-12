class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.ring_position = -1

    def append(self, item):
        self.ring_position += 1

        if self.ring_position >= self.capacity:
            self.ring_position = 0

        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.ring_position] = item

    def get(self):
        return self.storage
