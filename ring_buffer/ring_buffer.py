class RingBuffer:
    # def __init__(self, capacity):
    #     self.capacity = capacity
    #     self.storage = []
    #     self.size = 0

    # def append(self, item):
    #     self.size += 1
    #     if self.size - 1 < self.capacity:
    #         return self.storage.append(item)
    #     else:
    #         self.storage.pop()
    #         return self.storage.insert(0, item)

    # def get(self):
    #     if self.storage == 0:
    #         print('the list is empty')
    #     else:
    #         return self.storage
    def __init__(self, capacity):
        pass
        self.capacity = capacity
        self.current_index = 0
        self.storage = []

    def append(self, item):

        if len(self.storage) < self.capacity:
            self.storage.append(item)

        self.storage[self.current_index] = item

        self.current_index += 1

        if self.current_index > (self.capacity - 1):
            self.current_index = 0

    def get(self):
        return self.storage
