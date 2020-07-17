# General Case Ring Buffer Class
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    # Special Case Full Ring Buffer CLass
    class __Full:
        def append(self, item):
            self.data[self.current] = item
            self.current = (self.current + 1) 

        def get(self):
            return self.data[self.current:] + self.data[:self.current]

    def append(self, item):
        # general case
        self.data.append(item)
        # full capacity
        if len(self.data) == self.capacity:
            self.current = 0
            # changes class to __Full
            self.__class__ = self.__Full
        
    def get(self):
        return self.data


if __name__ == "__main__":
    buffer = RingBuffer(5)

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    buffer.append('d')
    buffer.append('e')
    buffer.append('f')
    buffer.append('g')
    buffer.append('h')
    buffer.append('i')
    

    print(buffer.get())


