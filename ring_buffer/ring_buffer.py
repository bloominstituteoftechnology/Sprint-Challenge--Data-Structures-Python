class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.full = False
        self.storage = []
        self.counter = 0

    def is_full(self):
        if len(self.storage) >= self.capacity:
            self.full = True

    def append(self, item):
        if not self.full:
            self.storage.append(item)
            self.is_full()
        else:
            self.storage[self.counter] = item
            self.counter += 1
            if self.counter >= self.capacity:
                self.counter = self.counter % self.capacity


    def get(self):
        if self.full:
            return self.storage
        else:
            return [x for x in self.storage if x is not None]
