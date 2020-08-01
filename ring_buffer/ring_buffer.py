class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.head = 0

    def append(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            self.queue[self.head] = item
            self.head = (self.head + 1) % self.capacity

    def get(self):
        return self.queue

