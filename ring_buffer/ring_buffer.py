class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # initialize the variable.
        self.data = [] # create an empty list to hold the data.
        self.index = 0 # create an index var with initial value of zero. 

    def append(self, item):
        if len(self.data) < self.capacity: # if we are less than the capacity of the list append item
            self.data.append(item)
        else: # if we are at or over capacity
            self.data[self.index] = item # overwrite existing item beginning at 0 index
            self.index += 1 # move index to next item in list
            if self.index == self.capacity: # check to see if we reached max capacity 
                self.index = 0 # if yes, reset index to 0

    def get(self):
        return self.data # return the list.