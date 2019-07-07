# RingBuffer has two methods, append and get
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

# The append method adds elements to the buffer
    def append(self, item):
        self.storage[self.current] = item
        if self.current >= len(self.storage)-1:
            self.current = 0
        else:
            self.current += 1

# The get method returns all of the elements in the buffer in a list in their given order.
    def get(self):
        return [v for v in self.storage if v is not None]

# Test: Ran 1 test in 0.000s
