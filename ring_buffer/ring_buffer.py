class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.next_item = 0

    def append(self, item):
        if len(self.cache) < self.capacity:
            self.cache.append(item)
            if self.next_item < (self.capacity - 1):
                self.next_item += 1
            else:
                self.next_item = 0
        else:
            self.cache.pop(self.next_item)
            self.cache.insert(self.next_item, item)
            if self.next_item < (self.capacity - 1):
                self.next_item +=1
            else:
                self.next_item = 0



    def get(self):
        return self.cache