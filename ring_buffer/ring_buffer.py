class RingBuffer: # a buffer with a dynamic size, so that when it fills up, adding another element must overwrite the first (oldest) one its useful for storing log and history info 
    def __init__(self, capacity): # sets the capacity to an empty list 
        self.capacity  = capacity 
        self.storage = []
        
    def append(self, item): 
        self.storage.append(item) # append an element at the end of the list
        if len(self.storage) == self.capacity:
            self.cur = 0
            self.__class__ = self.__Full
    
    def get(self): # returns a list of items from the oldest to newest 
            return self.storage
    class __Full: #checking the length of capacity in the list at its maximum 
        def __init__(self, n):
            raise 

        def append(self, x): # add a node for the newest value and removes the newest node 
            self.storage[self.cur] = x
            self.cur = (self.cur+1) % self.capacity

        def get(self): #returns a list of items from the oldest to newest 
            return self.storage

# Reference
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
# http://code.activestate.com/recipes/68429-ring-buffer/

