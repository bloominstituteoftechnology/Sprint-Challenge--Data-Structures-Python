class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity #max number
        self.arry = []     #empty arry to keep data
        self.last = 0  #last position

    def append(self, item):
        if len(self.arry) < self.capacity:
            self.arry.append(item)
        else:
            self.arry[self.last] = item 
        self.last += 1  # last position plus 1
        self.last = self.last % (self.capacity)#Divides left hand operand by right hand operand and returns remainder

    def get(self):
        return self.arry