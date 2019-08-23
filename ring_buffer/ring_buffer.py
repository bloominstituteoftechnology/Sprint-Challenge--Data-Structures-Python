class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
      # checks to see if the current is less than the ring buffer capacity, if it is then it appends it to the end of the list
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1
      # else, it overwrites the oldest value in the list, starting with index 0, then increments it to be ready to overwrite the next value in the list
        else:
            self.current = 0
            self.storage[self.current] = item
            self.current += 1

    def get(self):
        return [i for i in self.storage if i != None]
