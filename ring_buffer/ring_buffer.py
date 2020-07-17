class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.head = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.pop(self.head)
            self.storage.insert(self.head, item)
            self.head += 1
            if self.head == self.capacity:
                self.head = 0
        else:
            self.storage.append(item)

    def get(self):
        return self.storage