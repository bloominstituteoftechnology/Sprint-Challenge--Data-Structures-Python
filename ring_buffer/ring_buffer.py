class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current_pos = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.current_pos] = item
        
        self.current_pos += 1
        self.current_pos = self.current_pos % (self.capacity)

    def get(self):
        return self.data