class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest_index = 0

    def append(self, item):
        # append an item at the end of the buffer
        self.data.append(item)
        if len(self.data) == capacity:
            self.current = 0
            # permanently chang self class from not full to full
            self.__class__ = self.__Full

    def get(self):
        return self.data