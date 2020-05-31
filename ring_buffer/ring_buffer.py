class RingBuffer:
    def __init__(self, capacity):   
        self.capacity = capacity
        self.storage = []
        self.tracker = 0
        

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.tracker] = item
            if self.tracker + 1 == self.capacity:
                self.tracker = 0
            else: 
                self.tracker += 1
        else: 
            self.storage.append(item)
        return item

    def get(self):
        return self.storage

rb = RingBuffer(4)

rb.append(1)
rb.append(2)
rb.append(3)
rb.append(1)
rb.append(5)
rb.append(7)
rb.append(89)
rb.append(99)
rb.append(20)
rb.append(2)
rb.append(3)
rb.append(1)

print(rb.get())




