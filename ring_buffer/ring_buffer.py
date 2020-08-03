class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index_counter = 0

    def append(self, item):
        # Non-full ring buffer
        if len(self.data) < self.capacity:
            self.data.append(item)

        # Full ring buffer
        elif len(self.data) == self.capacity:
            self.data[self.index_counter] = item
            if self.index_counter == 4:
                self.index_counter = 0
            else:
                self.index_counter += 1

    def get(self):
        return self.data