class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    def append(self, item):
        # Use of %: Now every time we get to the end of the array we will automatically start back at zero, allowing us to circularly queue.
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        self.size = self.size + 1
        

    def get(self):
        # ignore all that are None
        result = []
        for item in self.queue:
            if item is not None:
                result.append(item)
        return result
            
