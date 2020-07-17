class RingBuffer:
    def __init__(self, capacity):
       self.capacity = capacity
       self.stuff = []
       self.oldest = 0

    def append(self, item):
         if len(self.stuff) < self.capacity:
            self.stuff.append(item)
         else:
            self.stuff.remove(self.stuff[self.oldest])
            self.stuff.insert(self.oldest, item)
            if self.oldest+1 < self.capacity:
                self.oldest += 1
            else:
                self.oldest = 0

    def get(self):
        return(self.stuff)