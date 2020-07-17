from queue import CircularQueue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = CircularQueue(capacity)

    def append(self, item):
        self.queue.enqueue(item)
        
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


if __name__ == "__main__":
    buffer = RingBuffer(5)

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    buffer.append('d')
    buffer.append('e')
    buffer.append('f')

    print(buffer.get())




