class RingBuffer:
    
    def __init__(self, capacity):
        # initialize variable with passed in data
        self.capacity = capacity
        # create an empty data structure to store data
        self.buffer = []
        # create a queue to store index location of where data should be appended
        self.queue = [index for index in range(capacity)]
    
    def append(self, item):
        # get index location where item should be inserted
        index = self.queue.pop(0) #dequeue
        self.queue.append(index) # enqueue
        
        # fill buffer before checking and replacing elements
        if len(self.buffer) < self.capacity:
        # add item to buffer at index location of oldest element
            self.buffer.insert(index, item)   
        else:
            self.buffer[index] = item # replace element at index location

    def get(self):
        # use filter method to remove None values if the exist
        return list(filter(None, self.buffer))



