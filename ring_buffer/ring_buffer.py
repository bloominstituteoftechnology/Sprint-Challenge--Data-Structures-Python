class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.counter = 0

    def append(self, item):
        if len(self.ring) < self.capacity:
            self.ring.append(item)
        else:
            self.ring[self.counter] = item
            self.counter += 1
        if self.counter == self.capacity:
            self.counter = 0

    def get(self):
        return(self.ring)

buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer.get())
buffer.append('d')
buffer.append('e')
print(buffer.get())