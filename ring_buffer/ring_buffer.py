class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.current = 0
        self.capacity = capacity

    def append(self, item):
        if len(self.data) != self.capacity: #check if capacity is full
            self.data.append(item) #recurse
        else:
            self.data[self.current] = item #write in element or overwrite oldest element
            self.current = (self.current+1) % self.capacity
        # 1 mod 5 = 1, 2 mod 5 = 2, 3 mod 5 = 3, etc, until it reaches 5 mod 5 (capacity) then 5 mod 5 = 0 and the first element (the oldest element) is now the place where the data is stored so element 0 is overwritten.

    def get(self):
        return self.data