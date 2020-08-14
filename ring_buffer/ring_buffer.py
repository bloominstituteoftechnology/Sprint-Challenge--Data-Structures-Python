
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.counter = 0

    def append(self, item):
        if len(self.arr) == self.capacity:
            self.arr[self.counter] = item
            if self.counter + 1 == self.capacity:
                self.counter = 0
            else:
                self.counter += 1
        else:
            self.arr.append(item)
        return item

    def get(self):
        return self.arr
