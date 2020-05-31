class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        # current is the index as we progress through the list
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = item
    
        if self.current < self.capacity - 1:
            self.current += 1
        else:
            self.current = 0


    def get(self):
        items = []
        for i in self.storage:
            if i is not None:
                items.append(i)
        print(items)
        return items