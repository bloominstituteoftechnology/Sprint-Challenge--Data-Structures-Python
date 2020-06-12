class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__storage = [None] * capacity
        self.__head = 0

    def append(self, item):
        self.__storage[self.__head] = item
        self.__head = (self.__head + 1) % self.capacity

    def get(self):
        start = None
        end = None
        for i, x in enumerate(self.__storage):
            if start is None and x is not None:
                start = i
            elif end is None and x is None:
                end = i
        return self.__storage[start:end]
