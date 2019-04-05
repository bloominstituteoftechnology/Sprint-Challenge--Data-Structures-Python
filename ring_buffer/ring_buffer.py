class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.capacity > self.current:
            self.storage.pop(0)
            self.storage.append(item)
            self.current += 1

        elif self.capacity == self.current:
            self.storage.pop(0)
            self.storage.insert(0, item)
            self.current += 1
        else:
            self.storage.pop(self.capacity - 1)
            self.storage.insert(0, item)

    def get(self):
        storage = self.storage
        storage = [x for x in storage if x is not None]
        return storage


buf = RingBuffer(4)


buf.append(1)
print(buf.get())
buf.append(1)
print(buf.get())
buf.append(3)
print(buf.get())
buf.append(6)
print(buf.get())
buf.append(10)
print(buf.get())
# buf.append(9)
# print(buf.get())
# buf.append(3)
# buf.append(6)
# print(buf.get())
