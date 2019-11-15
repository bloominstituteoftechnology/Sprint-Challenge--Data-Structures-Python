class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # Add item to list replacing the oldest item
        # self.storage[self.current] = item
        # self.current += 1
        # if self.current == self.capacity:  # if the capacity has been reached
        #   self.current = 0
        # else:
        #   self.current += 1
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1
        else:
            self.current = 0
            self.storage[self.current] = item
            self.current += 1

    def get(self):
        #
        all_elements = []
        if self.storage is not None:  # as long as its not None
            for i in self.storage:
                if i is not None:  # for each item not None append all_elements
                    all_elements.append(i)

        return all_elements
