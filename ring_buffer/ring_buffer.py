class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.arry = []     
        self.last = 0  

    def append(self, item):
        if len(self.arry) < self.capacity:
            self.arry.append(item)
        else:
            self.arry[self.last] = item 
        self.last += 1  
        self.last = self.last % (self.capacity)

    def get(self):
        return self.arry