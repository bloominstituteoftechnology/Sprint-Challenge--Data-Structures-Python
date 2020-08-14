class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        

        if len(self.data) >= self.capacity:
            self.data.pop(0) and self.data.insert(0, item)
            
        else:
            self.data.append(item)

    def get(self):
        return self.data