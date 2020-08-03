class RingBuffer:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.oldest = 0


    def append(self, item):
        self.buffer[self.oldest] = item

        if(self.oldest < self.capacity - 1):
            self.oldest += 1
        else:
            self.oldest = 0

    def get(self):
        clean_buffer = []
        for e in self.buffer:
            if e is not None:
                clean_buffer.append(e)

        return clean_buffer
