class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = -1
        self.buffer_array = []

    def append(self, item):
        if len(self.buffer_array) == self.capacity:
            self.current = (self.current + 1) % self.capacity
            self.buffer_array[self.current] = item
        else:
            self.buffer_array.append(item)

    def get(self):
        return self.buffer_array
