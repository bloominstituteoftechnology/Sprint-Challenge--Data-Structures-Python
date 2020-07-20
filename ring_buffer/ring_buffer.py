class RingBuffer:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.oldest_index = 0 

    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.oldest_index] = item
            self.oldest_index += 1

        if self.oldest_index == self.capacity:
            self.oldest_index = 0

    def get(self):
        return self.items