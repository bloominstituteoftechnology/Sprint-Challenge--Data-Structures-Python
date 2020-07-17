class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.position = 0  #index of current position


    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.position] = item

        self.position += 1

        if self.position == self.capacity:
            self.position = 0


    def get(self):
        return self.data