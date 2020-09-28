class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    oldest = 0

    def append(self, item):
        print("------")
        print(self.storage)
        print(len(self.storage))

        if len(self.storage) == self.capacity:
            self.storage.remove(self.storage[self.oldest])
            self.storage.insert(self.oldest, item)
            if self.oldest + 1 == 5:
                self.oldest = 0
            else:
                self.oldest += 1
            print("AFTER")
            print(self.storage)

        elif len(self.storage) == 0:
            self.storage.insert(0, item)

        else:
            self.storage.append(item)

    def get(self):
        if len(self.storage) == 0:
            return []

        else:
            return self.storage