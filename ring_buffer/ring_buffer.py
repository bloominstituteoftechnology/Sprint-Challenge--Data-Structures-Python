from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = list()[-capacity:]
        self.index = 0

    def append(self, item):
        if len(self.items) == self.capacity:
            self.items[self.index] = item
        else:
            self.items.append(item)
        self.index = (self.index + 1) % self.capacity


    def get(self):
        return self.items