class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        for x in self.buffer:
            x[1] -= 1 #* for x in buffer minus 1

        if len(self.buffer) < self.capacity: #* if length of the list is less than the capicity(5)
            self.buffer.append([item, self.capacity]) #* append the item and order it's added

        else:
            for x in range(len(self.buffer)): #* for x in range of the length of buffer
                if self.buffer[x][1] == 0: #* if buffer is equal to zero
                    self.buffer[x] = [item, self.capacity] #* replace the oldest item in the list


    def get(self):
        return [x[0] for x in self.buffer]

#* ALL TESTS PASSED