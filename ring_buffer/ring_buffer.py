import queue

class RingBuffer:
    def __init__(self, capacity, element=0):
        self.capacity = capacity
        self.items = []
        self.element = element


    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.element] = item
            self.element += 1
            if self.element == self.capacity:
                self.element = 0


    def get(self):
        return self.items