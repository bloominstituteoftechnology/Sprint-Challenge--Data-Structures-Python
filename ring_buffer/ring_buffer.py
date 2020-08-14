
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):

        if self.capacity == len(self.data):
            
     
        else:
            self.data.append(item)        
  

    def get(self):
        return self.data


