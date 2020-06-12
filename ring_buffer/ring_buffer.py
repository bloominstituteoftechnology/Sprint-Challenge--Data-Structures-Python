class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0


    def append(self, item):
        # if length of data is less than capacity
        if len(self.data) < self.capacity:
        # append item to data            
            self.data.append(item)
            return self.data
        elif len(self.data) == self.capacity:
            self.data[self.current] = item
            # if self.current == 4:
            #     self.current = 0
            # else: 
            self.current += 1
        

    def get(self):
        return self.data