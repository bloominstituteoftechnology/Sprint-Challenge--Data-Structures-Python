
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
      self.data.append(item) 
  

    def get(self):
        return self.data


