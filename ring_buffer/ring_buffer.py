class RingBuffer:
    #  define initial setting of the RingBuffer class
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.current = 0

    def get(self):
        # return a list of items from the oldest to the newest
        return self.data