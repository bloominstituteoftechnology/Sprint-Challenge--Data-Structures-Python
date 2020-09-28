class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.Item = -1

    def append(self, item):
        if self.capacity is len(self.data):
            self.Item = (self.Item + 1) % self.capacity
            self.data[self.Item] = item
        else:
            self.data.append(item)
            self.Item += 1

    def get(self):
        return self.data


# Test Code
buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']

buffer.append('g')
buffer.append('h')

print(buffer.get())   # should return ['d', 'e', 'f']
