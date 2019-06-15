class RingBuffer:
    def __init__(self, length):
        self.length = length
        self.count = 0
        self.storage = [None]*length

    def append(self, value):
        if self.count < self.length:
            self.storage[self.count] =  value
            self.count +=1
        else:
            self.count = 0
            self.storage[self.count] = value
            self.count += 1
        
    def get(self):

      return [i for i in self.storage if i != None]


buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']

