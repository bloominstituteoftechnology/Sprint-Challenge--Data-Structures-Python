class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest_id = 0

    def append(self, data):
        # if list is empty and data is not none, append
        if len(self.data) < self.capacity:
            self.data.append(data)
        # add one to oldest id index for new append
        else:
            self.data[self.oldest_id] = data
        self.oldest_id += 1
        # also if the set capacity is equal to oldest id, id = 0
        if self.oldest_id == self.capacity:
            self.oldest_id = 0

    def get(self):
        return self.data

# Testing

buffer = RingBuffer(3)
buffer.get()
buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())

buffer.append('d')

print(buffer.get())

buffer.append('e')
buffer.append('f')

print(buffer.get())
