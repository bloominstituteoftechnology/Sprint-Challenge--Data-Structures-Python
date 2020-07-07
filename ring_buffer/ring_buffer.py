class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = []
        self.counter = 0

    def append(self, item):
        if self.counter == 5:
            self.counter = 0
        if len(self.array) == 0:
            self.array.append(item)
        elif len(self.array) > 0 and len(self.array) < self.capacity:
            self.array.append(item)
        elif len(self.array) == self.capacity:
            self.array.pop(self.counter)
            self.array.insert(self.counter, item)
            self.counter +=1

    def get(self):
        if self.array[0] == int:
            self.array.sort()
            return self.array
        else:
            return self.array
