class RingBuffer:
    def __init__(self, capacity):
        self.q = list()
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.index = 0

    def iterate_head(self):
        if self.head >= self.capacity -1:
            self.head = 0
        else:
            self.head += 1

    def iterate_tail(self):
        if self.tail >= self.capacity - 1:
            self.tail = 0
        else:
            self.tail += 1

    def size(self):
        return len(self.q)

    def append(self, item):
        if self.size() == self.capacity:
            self.q[self.tail] = item
            self.iterate_tail()
        else:
            self.q.append(item)
            self.iterate_tail()

    def get(self):
        return self.q
            

