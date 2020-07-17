class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.counter = 0
        self.index = 0
        self.full = False

    def append(self, item):
        print(item)
        if self.full: 
            print('in full loop!')
            self.data[self.index] = item
            self.index += 1
            if self.index == self.capacity: 
                self.index = 0
        else: 
            print('before full loop!')
            self.data.append(item)
            self.counter += 1
            if self.counter == self.capacity:
                print('Full has been triggered!')
                self.full = True

    def get(self):
        return self.data