class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.queue_position = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.queue_position] = item
        self.queue_position += 1
        if self.queue_position == self.capacity:
            self.queue_position = 0

    def get(self):
        return self.storage