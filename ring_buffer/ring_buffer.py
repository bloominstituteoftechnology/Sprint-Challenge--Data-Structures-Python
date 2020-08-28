class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0 

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.index] = item
            self.index += 1
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        return self.storage

buffer = RingBuffer(3)
buffer.get()
buffer.append("Joe")
buffer.append("Heriberto")
buffer.append("Sean")
print(buffer.get())

buffer.append("James")
buffer.append("David")
print(buffer.get()) 