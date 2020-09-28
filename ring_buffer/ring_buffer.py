class RingBuffer:
    def __init__(self, capacity):
        self.list = []
        self.capacity = capacity
        self.counter = 0

    def append(self, item):
        if len(self.list) == self.capacity:
            self.list[self.counter] = item
            if self.counter + 1 == self.capacity:
                self.counter = 0
            else:
                self.counter +=1
        else:
            self.list.append(item)

    def get(self):
        return self.list