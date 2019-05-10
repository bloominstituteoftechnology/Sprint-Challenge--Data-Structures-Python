class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if len(self.get()) == 5:
            self.storage[self.current] = item
            self.current += 1
        else:
            self.storage[0] = self.storage[1]
            self.storage[1] = self.storage[2]
            self.storage[2] = self.storage[3]
            self.storage[3] = self.storage[4]
            self.storage[4] = item

    def get(self):
        temp = []
        for item in self.storage:
            if item is not None:
                temp.append(item)
        return temp


buffer = RingBuffer(5)
print(buffer.append('a'))
print(buffer.append('b'))
print(buffer.append('c'))
print(buffer.append('d'))
print(buffer.append('e'))
print(buffer.get())
print("--------")
print(buffer.append('f'))
# print(buffer.storage)
print(len(buffer.storage))
print(buffer.get())
print('---0---')
print(buffer.append('g'))
print(buffer.append('h'))
print(buffer.append('i'))
