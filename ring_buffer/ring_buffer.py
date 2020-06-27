class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0
        self.oldest = 0

    def append(self, item):
        self.size += 1
        # If the ring buffer isn't empty, add to the end of the list
        if self.size <= self.capacity:
            self.storage.append(item)
        # If ring is full, replace the element at the oldest index
        else:
            if self.oldest < self.capacity - 1:
                self.storage[self.oldest] = item
                self.oldest += 1
            else:
                self.storage[self.oldest] = item
                self.oldest = 0

    def get(self):
        return self.storage