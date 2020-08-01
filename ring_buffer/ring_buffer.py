class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.counter = 0

    def append(self, item):
        if len(self.items) == self.capacity:
           # for i in range(0, self.capacity):
            del self.items[self.counter]
            self.items.insert(self.counter, item)
            if self.counter == 4:
                self.counter = 0
            else:
                self.counter += 1
        else:
            self.items.append(item)

    def get(self):
        return self.items

x=RingBuffer(5)
x.append(1); x.append(2); x.append(3); x.append(4)
print(x.get())
x.append(5)
print(x.get())
x.append(6)
print(x.get())
x.append(7); x.append(8); x.append(9); x.append(10)
print(x.get())
x.append(8); x.append(9); x.append(10); x.append(11); x.append(12)
print(x.get())

