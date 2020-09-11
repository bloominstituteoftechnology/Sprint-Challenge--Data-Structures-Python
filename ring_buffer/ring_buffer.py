class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.old_data = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.old_data] = item
        else:
            self.data.append(item)
        self.old_data = (self.old_data + 1) % self.capacity

    def get(self):
        return self.data