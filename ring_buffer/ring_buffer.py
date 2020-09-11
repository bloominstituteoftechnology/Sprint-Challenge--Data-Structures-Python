class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0 
        self.buffer = []

#FIFO - First In First Out --> Similar to Queue
#When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element
       
    def append(self, item):
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
        #capacity = 5 / if the item to be added is the last index(5-1=4), make it the first
            self.buffer[self.index] = item
            if self.index == self.capacity - 1:
                self.index = 0
            else:
                self.index += 1

    def get(self):
       return self.buffer


