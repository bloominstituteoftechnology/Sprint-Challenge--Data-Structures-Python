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
        return array


if __name__ == "__main__":
    buffer = RingBuffer(5)

    buffer.append("a")
