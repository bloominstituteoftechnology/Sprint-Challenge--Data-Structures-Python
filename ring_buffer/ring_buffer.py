class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.curr = -1

    def append(self, item):
        # were at full capacity
        if len(self.data) == self.capacity:
            self.curr = (self.curr + 1) % self.capacity
            self.data[self.curr] = item
        else:
            self.data.append(item)

    def get(self):
        return self.data