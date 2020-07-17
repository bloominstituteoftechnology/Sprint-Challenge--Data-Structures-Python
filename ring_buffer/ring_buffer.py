from queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = Queue()

    def append(self, item):
        if self.queue.__len__() < self.capacity:
            self.queue.enqueue(item)

        else:
            self.queue.dequeue()
            self.storage.enqueue(item)
        
    def get(self):
        pass


if __name__ == "__main__":
    rb = RingBuffer(3)
    rb.append("a")
    rb.append("b")
    rb.append("c")

    print(rb.get())


