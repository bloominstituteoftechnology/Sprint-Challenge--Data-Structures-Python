class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.next_index_available = 0
        # Mimic creation of a C-style STATIC array 
        # (as the underlying data structure for our RingBuffer class):
        self.items = [None for item in range(capacity)]

    def append(self, item):
        # Add item:
        self.items[self.next_index_available] = item
        # Set next index, returning to the beginning of the buffer after exceeding available space:
        self.next_index_available += 1
        if self.next_index_available > (self.capacity - 1):
            self.next_index_available = 0

    def get(self):
        return list(filter(lambda x: x is not None, self.items))
        # Alternative method: return [item for item in self.items if item is not None]

    def __repr__(self):
        return f"RingBuffer: \ncapacity: {self.capacity} \nelements: \n{self.items}"
