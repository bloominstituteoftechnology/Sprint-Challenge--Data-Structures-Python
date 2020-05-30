class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current_node = 0
        pass

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.pop(self.current_node)
            self.storage.insert(self.current_node, item)
            self.current_node = (self.current_node + 1) % self.capacity
        else:
            self.storage.append(item)
        pass

    def get(self):
        return self.storage
        pass
    
    # ran test and came out .001s!
    
    