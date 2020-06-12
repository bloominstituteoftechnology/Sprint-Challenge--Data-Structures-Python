class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_index = 0
        self.buffer = []

    def append(self, item):
        
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)

        self.buffer[self.current_index] = item

        self.current_index += 1

        if self.current_index > (self.capacity - 1):

            self.current_index = 0
    def get(self):
        return self.buffer