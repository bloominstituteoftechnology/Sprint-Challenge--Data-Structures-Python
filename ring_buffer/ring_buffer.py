class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current > (self.capacity - 1):
            self.current = 0
            self.storage[self.current] = item
        else:
            try:
                self.storage[self.current] = item
            except IndexError:
                self.storage.append(item)
        self.current += 1

    def get(self):
        try:
            self.storage.remove(None)
        except:
            return self.storage
        return self.storage


buffer = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.get())


buffer.append('e')
print(buffer.get())
buffer.append('f')
print(buffer.get())
buffer.append('g')
buffer.append('h')
buffer.append('i')
print(buffer.get())
