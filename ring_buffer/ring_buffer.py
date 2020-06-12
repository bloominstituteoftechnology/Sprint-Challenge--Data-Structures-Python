class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.oldest = 0


    def append(self, item):
        #if buffer is at capacity
        if len(self.buffer) == self.capacity:
            #replace the oldest element with new item
            self.buffer[self.oldest] = item

            #change oldest to the new oldest in the buffer.
            #if self.oldest was at the end of the buffer list, then start over at the beginning of the list (position 0)
            if self.oldest == self.capacity - 1:
                self.oldest = 0
            #else, increase oldest position by 1
            else:
                self.oldest+=1
        #if buffer not yet at capacity, simply add the item
        else:
            self.buffer.append(item)


    def get(self):
        #filter out any None's in the buffer
        return [item for item in self.buffer if not None]