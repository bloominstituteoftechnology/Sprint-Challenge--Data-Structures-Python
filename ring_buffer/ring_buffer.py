class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = ['' for x in range(capacity)] # need to fill array to reference index
        self.pointer = 0
        

    def append(self, item):
        # ad item to array by pointer then increment
        self.storage[self.pointer] = item
        self.pointer += 1
        
        # if pointer exceeds capacity set to 0
        if self.pointer ==  self.capacity:
            self.pointer = 0

    def get(self):
        return [x for x in self.storage if x != '']