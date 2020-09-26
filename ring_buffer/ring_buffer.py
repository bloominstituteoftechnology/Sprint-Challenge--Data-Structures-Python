class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_index = 0
        self.storage = []

    def append(self, item):
        """  
            When buffer is full, place the value of `item` at the current index;
            otherwise, append the item to the end of the buffer
        """
        if len(self.storage) == self.capacity:
            self.storage[self.current_index] = item
            self.current_index = (self.current_index + 1) % self.capacity
        else:
            self.storage.append(item)

    def get(self):
        return self.storage