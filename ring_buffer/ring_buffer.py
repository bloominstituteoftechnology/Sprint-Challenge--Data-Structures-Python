class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.oldest = 0

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        elif len(self.list) == self.capacity and self.oldest < len(self.list):
            self.list[self.oldest] = item
            self.oldest += 1
        elif self.oldest == len(self.list):
            self.oldest = 0
            self.list[self.oldest] = item
            self.oldest += 1

    def get(self):
        # print(self.list)
        # print(self.capacity)
        # print(self.oldest)
        # print(len(self.list))
        return self.list


# r = RingBuffer(3)
# r.append('a')
# r.append('b')
# r.append('c')
# r.append('d')
# r.append('e')
# r.append('f')
# r.append('h')
# r.append('i')


# r.get()
