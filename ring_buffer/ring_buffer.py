class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.clock = 0
        self.stack = []

    def append(self, item):
        # Check if we're not past our capacity
        if len(self.stack) < self.capacity:
            # Check if item isn't already on the list:
            if item not in self.stack:
                self.stack.append(item)
            # If item is in list, pop it out of the list and append returned value
            else:
                self.stack.append(self.stack.pop(item))
        # If we're past capacity, delete index 0 and call append again
        else:
            #check if item in stack already
            if item not in self.stack:
                self.stack[self.clock] = item
                self.update_clock()
            else:
                self.stack.append(self.stack.pop(item))

    def get(self):
        return self.stack

    def update_clock(self):
        self.clock = self.clock + 1 if self.clock + 1 < self.capacity else 0