class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Create an empty list for items to be stored in.
        # If len(self.storage) is less than capaacity, the length should be as
        #. long as the number of items added to it. Other than that,
        #. len(self.storage) should always be the capacity size
        self.storage = [][:capacity]
        # store the index as an attribute (start at 0) so we can keep track of
        #. where we are putting the incoming item
        self.index = 0

    def append(self, item):
        
        # if the length of our storage is already max, change item at oldest
        #. index to that item
        if len(self.storage) == self.capacity:
            self.storage[self.index] = item
        # otherwise, just append the item to the storage list
        else:
            self.storage.append(item)
        
        # update index of item so RingBuffer knows where to add the new item if
        #. capacity is full.
        # EXAMPLE: capacity is 2. First index was 0, and length < 2, so we
        #. append to the empty list. Then update index. (0 + 1) % 2 = 1. New
        #. index is 1. Length < 2 still so next item will be appended. Update
        #. index again. (1 +1) % 2 = 0. So new index will be 0. Length now
        #. equals capacity so we change the item at new index (0). 
        self.index = (self.index + 1) % self.capacity

    def get(self):
        # return the list of items
        return self.storage