class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.storage = []

    def append(self, item):
        # if full
        if len(self.storage) == self.capacity:
            self.storage[self.index] = item
        # if not
        else:
            self.storage.append(item)
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return self.storage


if __name__ == '__main__':
    buffer = RingBuffer(3)

    print(buffer.get())  # should return []

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    print(len(buffer.get()))
    print(buffer.get())  # should return ['a', 'b', 'c']

    # 'd' overwrites the oldest value in the ring buffer, which is 'a'
    buffer.append('d')

    print(buffer.get())  # should return ['d', 'b', 'c']

    buffer.append('e')
    print(buffer.get())
    buffer.append('f')

    print(buffer.get())  # should return ['d', 'e', 'f']