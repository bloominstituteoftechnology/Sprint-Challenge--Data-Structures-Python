class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.current = 0

    def append(self, item):
        # if the queue is not full, append the item. current position does not need to be updated
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:  # if the queue is full, append the new item to the item at current index, which is the oldest item in the queue
            self.queue[self.current] = item

        self.current += 1
        # current position will not exceed capacity
        self.current = self.current % self.capacity

    def get(self):
        return self.queue
