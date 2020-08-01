class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.index = 0

    def append(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            self.queue[self.index] = item
            self.index = (self.index+1) % self.capacity

    def get(self): #return the queue
        return self.queue