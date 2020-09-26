class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cur = 0
        self.data = [None]* capacity

    def append(self, item):
        if self.cur == self.capacity:
            self.cur = 0
        self.data[self.cur]= item
        self.cur += 1

    def get(self):
        while None in self.data:
            self.data.remove(None)

        return self.data
    