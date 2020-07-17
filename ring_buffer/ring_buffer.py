class RingBuffer:    
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0 
        self.storage = [None] * capacity

    def append(self, item):
        if self.index >= self.capacity:
            self.index = 0
        self.storage[self.index] = item
        self.index += 1

    def get(self):
        return [item for item in self.storage if item is not None] 

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())
