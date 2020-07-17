class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity   
        self.oldest_index = 0

    def append(self, item):
        # append an item at the end of the buffer
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.oldest_index] = item
            self.oldest_index +=1
        if self.oldest_index == self.capacity:
            self.oldest_index = 0
            

    def get(self):
        return self.data