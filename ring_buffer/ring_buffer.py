class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.newNum = 0
        self.list = [None for i in range(capacity)]

    def append(self, item):
        self.list[self.newNum] = item
        self.newNum += 1
        if self.newNum == self.capacity:
            self.newNum = 0

    def get(self):
        return [i for i in self.list if i != None]

buffer = RingBuffer(5)
for i in range(100):
    buffer.append(i)
    buffer.get()
    print(buffer.list)