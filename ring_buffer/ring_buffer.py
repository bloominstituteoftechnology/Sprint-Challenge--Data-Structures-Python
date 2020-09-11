
class RingBuffer:
    
    def __init__(self, capacity, storage=None, temp=0):
        self.capacity = capacity
        self.storage = []
        self.temp = temp
   
    def append(self, item):
        self.storage.append(item)
        if len(self.storage) > self.capacity:
            self.storage[self.temp] = item
            self.storage.pop()          
            self.temp += 1
        if self.temp > self.capacity:
            self.temp = 0
        
    
    def get(self):
        return self.storage