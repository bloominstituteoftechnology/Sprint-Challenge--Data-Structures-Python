class RingBuffer:
    counter = 0
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0


    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.index] = item
        else:
            self.storage.append(item)
        # add item to the index after the one it's at
        self.index = (self.index + 1) % self.capacity
    

    def get(self):
        ''' Returns all elements in the buffer 
        as a list in their given order
        '''
        return self.storage

buffer = RingBuffer(3)
buffer.append('g')
buffer.append('a')
buffer.append('s')
buffer.append('k')
print(buffer.get())