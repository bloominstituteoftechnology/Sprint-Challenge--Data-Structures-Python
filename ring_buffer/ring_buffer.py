
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.location = 0

    def append(self, item):
        
        if self.capacity == len(self.data): 
            if self.location < self.capacity - 1:
                self.data[self.location] = item
                self.location += 1
            else:
                self.data[self.location] = item
                self.location = 0
         

        else:
            self.data.append(item)        
  

    def get(self):
        return self.data


