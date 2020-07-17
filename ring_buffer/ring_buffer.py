
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.tracking_index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.tracking_index] = item
        self.tracking_index += 1
        if self.tracking_index == self.capacity:
            self.tracking_index = 0

    def get(self):
        return self.storage


buffer = RingBuffer(3)
buffer.get()
buffer.append("a")
buffer.append("b")
buffer.append("c")
buffer.append("d")
print(buffer.get())
buffer.append("e")
buffer.append("f")
print(buffer.get())