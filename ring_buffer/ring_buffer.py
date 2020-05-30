class RingBuffer:
    def __init__(self, capacity):
            self.capacity = capacity
            self.count = 0
            self.storage = [None]*capacity

    def append(self, item):
        if self.count < self.capacity:
            self.storage[self.count] =  item
            self.count +=1
        else:
            self.count = 0
            self.storage[self.count] = item
            self.count += 1

    def get(self):
        return [i for i in self.storage if i != None]