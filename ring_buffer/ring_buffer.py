class RingBuffer:
    """ class that implements a not-yet-full buffer """
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = []


    class __Full:
        """ class that implements a full buffer """
        def append(self, x):
            """ Append an element overwriting the oldest one. """
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.capacity
        def get(self):
            """ return list of elements in correct order """
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
        """append an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.capacity:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data

# sample usage
if __name__=='__main__':
    x=RingBuffer(5)
    x.append(1); x.append(2); x.append(3); x.append(4)
    print(x.__class__, x.get())
    x.append(5)
    print(x.__class__, x.get())
    x.append(6)
    print(x.data, x.get())
    x.append(7); x.append(8); x.append(9); x.append(10)
    print(x.data, x.get())
