class RingBuffer:
    #A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # append method adds elements to the buffer.
        self.storage[self.current] = item
        self.current = self.current + 1
        # resets it back to the zero index to be replaced when the other items have been over-written
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        # returns all elements in queue except none in their given order
        return [x for x in self.storage if x != None]


buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']
