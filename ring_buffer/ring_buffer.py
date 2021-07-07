class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def append(self, item):
        self.items.append(item)
        if len(self.items) == self.capacity:
            self.cur = 0
            self.__class__ = RingBufferFull

    def get(self):
        return self.items


class RingBufferFull:
    def __init__(self, n):
        return 'Error'

    def append(self, item):
        self.items[self.cur] = item
        self.cur = (self.cur + 1) % self.capacity

    def get(self):
        return self.items[:self.cur] + self.items[self.cur:]