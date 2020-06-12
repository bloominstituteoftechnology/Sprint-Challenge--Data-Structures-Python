class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_node = None
        self.new_oldest_node = None
        self.stack = []

    def append(self, item):
        if self.oldest_node is None:
            self.oldest_node = 0
            return self.stack.append(item)

        elif len(self.stack) +1 <= self.capacity:
            self.new_oldest_node = 1
            return self.stack.append(item)
        
        else:
            self.stack[self.oldest_node] = item
            self.oldest_node += 1
            if self.oldest_node + 1 > self.capacity:
                self.oldest_node = 0
                
    def get(self):
        return self.stack
            