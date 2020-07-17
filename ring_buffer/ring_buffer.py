class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.size = 0
        
        #self.head = 0
        #self.tail = -1
        #self.data = [0 for i in range(capacity)]

    def append(self, item):
        if self.capacity == self.size:
            self.data.pop(0)
            self.data.insert(0, item) 
        else:
            self.data.append(item)
            self.size += 1

    def get(self):
        if self.size > 0:
            return self.data
