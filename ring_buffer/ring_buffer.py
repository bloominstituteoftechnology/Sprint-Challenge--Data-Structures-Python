class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.index] = item
            self.index +=1
            if self.index > (self.capacity) - 1:
                self.index = 0

    def get(self):
        return self.data