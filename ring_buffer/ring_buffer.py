from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = deque([])

    def append(self, item):
        # self.storage is not at capacity
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        # self.storage is at capacity
        
    def get(self):
        return list(self.storage)


if __name__ == "__main__":
    rb = RingBuffer(3)
    rb.append("a")
    rb.append("b")
    rb.append("c")

    print(rb.get())
