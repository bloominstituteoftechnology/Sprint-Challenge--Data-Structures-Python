class RingBuffer:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.size = 0
        self.write_index = 0
        self.storage = []

    def append(self, item):
        if self.size >= self.capacity:
            self.storage[self.write_index] = item
        else:
            self.storage.append(item)
            self.size += 1
            
        if self.write_index < (self.capacity - 1):
            self.write_index += 1
        else:
            self.write_index = 0

    def get(self):
        return self.storage