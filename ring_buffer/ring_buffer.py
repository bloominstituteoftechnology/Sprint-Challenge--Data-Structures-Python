class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = list()
        self.count = 0
        self.full = False

    def __str__(self):
        return f"{self.buffer}"

    def append(self, item):
        if len(self.buffer) is self.capacity:
            self.full = True
        if self.full is True:

            self.buffer.pop(self.count)
            self.buffer.insert(self.count, item)
            self.count += 1
            if self.count is self.capacity:
                self.count = 0
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)

    def get(self):
        return self.buffer


rb = RingBuffer(3)

rb.append(7)
rb.append(12)
rb.append(21)
print(rb)
rb.append(87)
print(rb)
rb.append(32)
print(rb)
rb.append(90)
print(rb)
rb.append(11)
print(rb)
rb.append(7)
print(rb)
