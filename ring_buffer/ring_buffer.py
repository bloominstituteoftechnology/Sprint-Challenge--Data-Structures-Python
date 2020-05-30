class RingBuffer:
    def __init__(self, capacity):  #Default
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item): #overwrites oldest node
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self): #returns new values after append
        return [x for x in self.storage if x is not None]
