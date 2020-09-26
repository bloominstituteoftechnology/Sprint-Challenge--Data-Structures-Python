class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.index = 0


    def append(self, item):
        if len(self.arr) is self.capacity:
            self.arr[self.index] = item
            self.index = (self.index + 1) % self.capacity
        else:
            self.arr.append(item)

    def get(self):
        return self.arr