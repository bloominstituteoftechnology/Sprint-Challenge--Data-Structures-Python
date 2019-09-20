class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):  # Adds the element to the buffer
      # current index is item
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0  # makes current to 0 and restarts

    # Returns all the elements in the buffer in a list in their given order. No none values.

    def get(self):
        buffer = []
        for i in self.storage:
            if i != None:
                buffer.append(i)

        return buffer
