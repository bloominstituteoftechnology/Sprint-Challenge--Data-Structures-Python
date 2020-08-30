class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.pointer = 0
        self.length = 0

    def append(self, item):
        if self.length < self.capacity:
            self.storage.append(item)
            self.length += 1
        else:
            self.storage[self.pointer] = item
            self.pointer += 1
            if self.pointer == self.capacity:
                self.pointer = 0

    def get(self):
        return self.storage
