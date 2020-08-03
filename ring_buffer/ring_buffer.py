class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.head = 0

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        else:
            self.list[self.head] = item
            self.head = (self.head + 1) % self.capacity

    def get(self):
        return self.list