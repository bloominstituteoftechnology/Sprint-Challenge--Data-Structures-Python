class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index =0
    
     
    def append(self, item):
        # check if the buffer is full
        if len(self.data) == self.capacity: 
            # overwrite the past value  with new item       
            self.data.pop(self.index)
            self.data.insert(self.index,item)
            self.index  = (self.index +1 ) % self.capacity
        else:
            self.data.append(item)
        
    def get(self):
        return self.data

buffer = RingBuffer(3)
print(buffer.get())
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer.get())
buffer.append('d')
print(buffer.get())

buffer.append('e')
print(buffer.get())