class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # we replace the element according to self.current (current index) with "item"
        self.storage[self.current] = item
        # if we're below capacity (accordint to index == capacity -1)
        if self.current < (self.capacity -1):
            # increase current index by 1
            self.current += 1
        else:
            # once we reach our limit we set current index back to 0
            # so we can proceed to replace oldest element
            self.current = 0
    def get(self):
        # if last item in storage is not None that means no more nones in list
        if self.storage[-1] != None:
            # we return entire list
            return self.storage
        else:
            # otherwise we return only to the point we've filled with new elements
            return self.storage[:self.current]