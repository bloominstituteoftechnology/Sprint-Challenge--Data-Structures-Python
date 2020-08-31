class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.counter = 0
    def append(self, item):
        if len(self.arr) == self.capacity:
            self.arr[self.counter] = item
            """ Above code is same as the commented code """
            # self.arr.pop(self.counter)
            # self.arr.insert(self.counter, item)
            if self.counter + 1 == self.capacity:
                self.counter = 0
            else:
                self.counter += 1
        else:
            self.arr.append(item)
        return item         

    def get(self):
        return self.arr

rb = RingBuffer(3)

rb.append(2)
rb.append(1)
rb.append(4)
rb.append(5)
rb.append(6)
rb.append(7)
rb.append(8)

print(f"{rb.get()}")
