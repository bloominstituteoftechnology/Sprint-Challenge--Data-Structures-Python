class RingBuffer:
    def __init__(self, capacity):

        self.capacity = capacity
        self.length = 0
        self.storage = list()
        # counter for knowing last placed value
        self.counter = 0


    def append(self, item):

        # when not at capacity 
        if self.length < self.capacity:
            self.storage.append(item)
            self.counter += 1
            self.length += 1

        # when at capacity
        elif self.length == self.capacity:
            # if counter is at the end:
            if self.counter == self.capacity:
                # move to beginning
                self.counter = 0
            # place item at counter index in storage
            self.storage[self.counter] = item
            self.counter += 1

    def get(self):
        
        return self.storage