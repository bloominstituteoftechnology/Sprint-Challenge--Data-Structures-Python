class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        #data is to fill in Nones rn

    def append(self, item):
        if self.capacity == self.size:
            #basically if its 0
            self.data[0] = item
            self.size = 1
        else:
            self.data[self.size] = item
            self.size += 1

    def get(self):
        if self.size > 0:
            return [i for i in self.data if i is not None]
            #don't count Nones
