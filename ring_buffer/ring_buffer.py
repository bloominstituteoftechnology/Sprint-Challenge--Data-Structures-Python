#FiFo - Circular Queue - Capacity of 5 in test
class RingBuffer:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.indexToOverwrite = 0 #FiFo, where 0 will be first item

    def append(self, item):
        queueSize = len(self.queue)
        if queueSize < self.capacity:
            self.queue.append(item)
        else: #if queueSize is at capacity:
            self.queue[self.indexToOverwrite] = item
            self.indexToOverwrite += 1

        #check to see if indexToOverwrite needs to be reset
        if self.indexToOverwrite == self.capacity:
            self.indexToOverwrite = 0

    def get(self):
        return self.queue