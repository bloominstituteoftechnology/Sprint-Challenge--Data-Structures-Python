class RingBuffer:
    def __init__(self, capacity):
        # init items
        self.items = []
        # init max capacity
        self.capacity = capacity
        # init the oldest element
        self.oldest = 0

    def append(self, item):
        # check if len is less than the current capacity then add an item
        if len(self.items) < self.capacity:
            self.items.append(item)
        # place oldest item and add 1 position
        else:
            self.items[self.oldest] = item
            self.oldest += 1
        # if oldest position 
        if self.oldest == self.capacity:
            self.oldest = 0

    def get(self):
        # return data
        return self.items



    # A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.