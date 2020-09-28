class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # capacity : max number in the buffer
        self.data = []     # empty storage for appending data later
        self.current_pos = 0  # current position index

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)

        else:
            self.data[self.current_pos] = item  # the oldest one's position starting from 0

        self.current_pos += 1  # then position plus 1
        self.current_pos = self.current_pos % (self.capacity)

    def get(self):
        # return list of elements in correct order 
        return self.data