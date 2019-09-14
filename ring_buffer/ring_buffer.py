class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # place the value of the input item into the proper location
        self.storage[self.current] = item
        # increment the index
        self.current += 1
        # if the current inexed is at capacity, reset the index
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        if self == None:
            return self.storage
        else:
            no_more_Nones = [i for i in self.storage if i != None]
            return no_more_Nones
