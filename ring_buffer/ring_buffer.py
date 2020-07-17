#FiFo - Circular Queue
class RingBuffer:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.indexOfOldestItem = 0 #FiFo, where index 0 will be first item in and out

    def append(self, item):
        if len(self.queue) < self.capacity: #is there space available?
            self.queue.append(item)
        else: #if queueSize is at capacity:
            self.queue[self.indexOfOldestItem] = item #append by overwriting oldest item
            #update indexOfOldestItem
            shouldReset = True if self.indexOfOldestItem == self.capacity else False
            self.indexOfOldestItem = 0 if shouldReset else self.indexOfOldestItem + 1

    def get(self):
        return self.queue