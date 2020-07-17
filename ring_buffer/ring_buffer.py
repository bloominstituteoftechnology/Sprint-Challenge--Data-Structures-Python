class RingBuffer:
    def __init__(self, capacity):
        self.last_item = 0 # oldest item is at index 0
        self.capacity = capacity
        self.store = []


    def append(self, item):
        if len(self.store) < self.capacity:
            self.store.append(item) # stores new item when there is space available in capacity
        else:   # capacity and store either full or store has more items than capacity
            self.store[self.last_item] = item
            if self.last_item < (len(self.store) - 1):
                self.last_item += 1
            else:
                self.last_item = 0

    def get(self):
        return(self.store)