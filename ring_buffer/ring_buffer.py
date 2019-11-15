class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    # adds elements to the buffer
    def append(self, item):
        storageLength = len(self.storage)

        for i in range(0, storageLength):
            # if the current storage is at capacity
            if self.storage[i] == None:
                self.storage[i] = item
                print(f"for i[{i}] in self.storage: {self.storage}")
                return
        # append to current oldest index
        self.storage[self.current] = item
        # next index is now the oldest
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1
        pass

    # returns all of the elements in the buffer in a list in their given order
    #    if None value is present, don't return it
    def get(self):
        result = []
        for element in self.storage:
            if element is not None:
                result.append(element)

        return result
        pass

