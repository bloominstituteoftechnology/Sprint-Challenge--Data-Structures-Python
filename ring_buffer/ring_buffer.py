class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage.pop(self.current)
        self.storage.insert(self.current, item)

        if self.current == len(self.storage) - 1:
            self.current = 0
        else:
            self.current += 1



    def get(self):
        return [x for x in self.storage if x is not None]


buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())

buffer.append('d')
print(buffer.get())

buffer.append('e')
buffer.append('f')

print(buffer.get())