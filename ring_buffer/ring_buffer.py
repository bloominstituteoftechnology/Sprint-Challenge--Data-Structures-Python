class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = [None] * capacity
        self.x = 0

    def append(self, item):
        #initialize list, have x rep the order in the array
        self.list[self.x] = item

        #if the place in the array = capacity, then set x to 0 to start the loop over
        if self.x + 1 == self.capacity:
            self.x = 0
        #then increment it each time
        else:
            self.x = self.x + 1

    def get(self):
        return [item for item in (self.list) if item is not None]