class RingBuffer:
    def __init__(self, capacity):
        self.data = [None for i in range(capacity)]

    def append(self, item):
        self.data.append(item)
        self.data.pop(0)

    def get(self):
        return self.data