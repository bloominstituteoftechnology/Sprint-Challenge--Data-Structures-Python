class RingBuffer:
    def __init__(self, capacity, count=0, storage=[]):
        self.storage = storage
        self.capacity = capacity
        self.count = count

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage.pop(self.count % self.capacity)
            self.storage.insert(self.count % self.capacity, item)
            self.count +=1

    def get(self):
        return self.storage