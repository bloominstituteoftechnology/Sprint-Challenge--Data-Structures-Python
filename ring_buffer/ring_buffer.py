class RingBuffer:
    def __init__(self, capacity):
        self.q = list()
        self.capacity = capacity
        self.head = 0
        self.tail = 0

    def iterate_head(self):
        if self.head == self.capacity:
            self.head = 0
        else:
            self.head += 1

    def iterate_tail(self):
        if self.tail == self.capacity:
            self.tail = 0
        else:
            self.tail += 1

    def append(self, item):
        pass

    def get(self):
        pass