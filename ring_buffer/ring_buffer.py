class RingBuffer:
    #  define initial setting of the RingBuffer class
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0

    def append(self, item):
        # if the current length of the list is less than the capacity, 
        # append item to the tail
        # otherwise, append item to tail and remove head
        if len(self.data) < self.capacity: 
            self.data.append(item)
        else:
            self.data[self.current] = item
            self.current += 1
            if self.current > (self.capacity) - 1:
                self.current = 0

    def get(self):
        # return a list of items from the oldest to the newest
        return self.data



# Sources:

    # 1. https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
    # 2. http://code.activestate.com/recipes/68429-ring-buffer/
    # 3. https://codereview.stackexchange.com/questions/85068/efficient-ring-buffer-fifo
    # 4. http://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/
