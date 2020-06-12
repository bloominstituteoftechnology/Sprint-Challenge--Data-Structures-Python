class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.old = 0


    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.old] = item
            if self.old < len(self.storage) - 1:
                self.old += 1
            else:
                self.old = 0


    def get(self):
        pass