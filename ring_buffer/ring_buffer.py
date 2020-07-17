class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        self.run = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data.pop(self.run)
            self.data.insert(self.run, item)
            if self.run < self.capacity - 1:
                self.run += 1
            else:
                self.run = 0

    def get(self):
        return self.data