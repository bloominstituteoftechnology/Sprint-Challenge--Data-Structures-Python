class RingBuffer:
    def __init__(self, capacity):
        self.capacity: int = capacity
        self.storage = []
        self.current_location = 0

    def append(self, item):
        if self.current_location >= len(self.storage):
            self.storage.append(item)
        else:
            self.storage[self.current_location] = item

        self.current_location += 1
        if self.current_location == self.capacity:
            self.current_location = 0

    def get(self):
        return self.storage