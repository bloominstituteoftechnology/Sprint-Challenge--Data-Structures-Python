class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.insertion_index = 0
    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.insertion_index] = item
            self.insertion_index += 1
            if self.insertion_index > (self.capacity - 1):
                self.insertion_index = 0

    def get(self):
        return self.storage
