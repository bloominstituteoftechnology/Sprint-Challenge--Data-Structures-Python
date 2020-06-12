class RingBuffer:
    def __init__(self, capacity, data=[]):
        self.index = 0
        self.capacity = capacity
        self.data = list(data)[capacity:]

    def append(self, value):
        if len(self.data) == self.capacity:
            self.data[self.index] = value
        else:
            self.data.append(value)
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return(self.data)