class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.curr = 0

    def append(self, item):
        self.storage[self.curr] = item 
        self.curr += 1
        if self.curr == self.capacity:
            self.curr=0

    def get(self):
        return [x for x in self.storage if x is not None]