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
