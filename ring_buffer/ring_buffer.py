class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.last_item_index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.last_item_index] = item
        self.increase_index()

    def get(self):
        return self.storage

    def increase_index(self):
        if self.last_item_index + 1 < self.capacity:
            self.last_item_index += 1
        else:
            self.last_item_index = 0
