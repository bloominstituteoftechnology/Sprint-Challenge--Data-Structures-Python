class RingBuffer:
    def __init__(self, capacity):
        self.index = 0
        self.capacity = capacity
        self.data = []

    def append(self, item):

        # check if full, if so replace oldest index
        if len(self.data) == self.capacity:
            self.data[self.index] = item

        # if not full, append item to list
        else:
            self.data.append(item)

        # keep track of oldest append
        # index increment +1 up to capacity, then restarts to 0
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return self.data


buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())

buffer.append('d')

print(buffer.get())

buffer.append('e')
buffer.append('f')

print(buffer.get())
