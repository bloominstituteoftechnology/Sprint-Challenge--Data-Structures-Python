# Approach with an array
# Debt owed to https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
class RingBuffer:
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = []

    class __Full:
        def append(self, item):
            self.array[self.current] = item
            self.current = (self.current + 1) % self.capacity
        def get(self):
            return self.array

    def append(self, item):
        self.array.append(item)
        if len(self.array) == self.capacity:
            self.current = 0
            self.__class__ = self.__Full

    def get(self):
        return self.array
