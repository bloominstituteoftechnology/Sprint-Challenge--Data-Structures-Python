class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def append(self, item):
        # Check if we're not past our capacity
        if len(self.stack) <= self.capacity:
            # Check if item isn't already on the list:
            if item not in self.stack:
                self.stack.append(item)
            # If item is in list, pop it out of the list and append returned value
            else:
                self.stack.append(self.stack.pop(item))
        # If we're past capacity, delete index 0 and call append again
        else:
            self.stack.pop(0)
            self.append(item)

    def get(self):
        pass