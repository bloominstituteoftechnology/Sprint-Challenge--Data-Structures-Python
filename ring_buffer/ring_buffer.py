class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.capacity > len(self.storage):
            self.storage.append(item)
            self.current += 1
        else:
            self.storage[self.current] = item
            self.current = ((self.current + 1) % self.capacity)

    def get(self):
        values = []
        for x in self.storage:
            if x is not None:
                values.append(x)
        return values