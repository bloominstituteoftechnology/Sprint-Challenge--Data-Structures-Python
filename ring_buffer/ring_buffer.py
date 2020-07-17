class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        if self.capacity > 0:
            if self.current < self.capacity:
                self.storage[self.current] = item
                self.current += 1  
            elif self.current == self.capacity:
                self.current = 0
                self.storage[self.current] = item
                self.current += 1
        else:
            return None
    def get(self):
        storage_none_removed = []
        for i in self.storage:
            if i:
                storage_none_removed.append(i)
        return storage_none_removed