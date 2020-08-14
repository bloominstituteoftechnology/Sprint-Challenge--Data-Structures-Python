
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # initialize variable
        self.storage = [] # Empty list to hold the data
        self.index = 0 # This is an index variable with initial value of zero.


    def append(self, item):
        # if  the length of storage is less than capacity append item to list
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else: # This is for if we are at or over capacity
            self.storage[self.index] = item # This is overwriting the existing item beginning at index 0 
            self.index += 1 # move the index to the next item in list
            if self.index == self.capacity: # This is checking if the index has reached max capacity
                self.index = 0 # if the answer is yes, we want to reset the index to 0

    def get(self):
        # return the list.
        return self.storage
