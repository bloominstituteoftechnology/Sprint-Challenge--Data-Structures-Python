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
