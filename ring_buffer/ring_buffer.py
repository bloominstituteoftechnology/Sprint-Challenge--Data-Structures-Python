from queue import CircularQueue

# Approach with CircularQueue class
class RingBuffer_:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = CircularQueue(capacity)

    def append(self, item):
        self.queue.enqueue(item)
        if self.queue.__len__() == self.capacity:
            self.queue.dequeue()
              
    def get(self):
        array = []
        current = self.queue.storage.head
        array.append(current.value)
        
        if current.get_next():
            while current.get_next() is not self.queue.storage.head:
                current = current.get_next()
                array.append(current.value)
                array = array[-1:] + array[:-1]
        return array


# Approach with an array
# Debt owed to https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
class RingBuffer:
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = []

    class __Full:
        def append(self, item):
            self.array[self.current] = item
            self.current = (self.current + 1) % self.capacity
        def get(self):
            return self.array

    def append(self, item):
        self.array.append(item)
        if len(self.array) == self.capacity:
            self.current = 0
            self.__class__ = self.__Full

    def get(self):
        return self.array


if __name__ == "__main__":
    buffer = RingBuffer(5)

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    buffer.append('d')
    buffer.append('e')
    buffer.append('f')

    print(buffer.get())

    print("\n")

    buffer = RingBuffer_(5)

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    buffer.append('d')
    buffer.append('e')
    buffer.append('f')

    print(buffer.get())






